#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright Huawei Technologies Co., Ltd. 2023-2050. All rights reserved.
"""制品（制品包）添加构建签名CMS

必要软件：
JAVA
PYTHON
SIGN_PLUGIN_HOME环境及环境变量
7z

使用方法：
传参的用法

一、 结果目录 输出包路径 : python artifacts_sign_cms.py -r "/usr1/workspace/target/smartkit_toolbox" -p "/usr1/shared/smartkit_toolbox.zip"
二、 包路径 输出包路径 : python artifacts_sign_cms.py -r "/usr1/workspace/target/smartkit_toolbox.zip" -p "/usr1/shared/smartkit_toolbox.zip"
三、 包路径 （输出为原路径）python artifacts_sign_cms.py -r "/usr1/workspace/target/smartkit_toolbox.zip"
四、 包匹配路径 （输出为原路径）python artifacts_sign_cms.py -r "/usr1/workspace/target/*.zip"
"""

import os
import argparse
import sys
import subprocess
import hashlib
import json
import stat
import shutil
import shlex
from pathlib import Path
import logging as log
import xml.etree.ElementTree as ET

log.basicConfig(level=log.INFO)
default_workspace = r"d:\workspace" if sys.platform == "win32" else "/usr1/workspace"
WORKSPACE = os.getenv("WORKSPACE", default_workspace)
SIGN_PLUGIN_HOME = os.getenv("SIGN_PLUGIN_HOME", os.getenv("SIGNATURE_HOME"))
s = os.sep


def execute_command(cmd: str, working_dir: str = WORKSPACE) -> None:
    """仅执行系统命令,无返回结果,有报错机制,采用shlex.split所以windows路径请用双引号引起来"""
    log.info("execute current_dir: %s", working_dir)

    if sys.platform == "win32":
        shell_prefix = ["cmd", "/c"]
        cmd_split = shlex.split(cmd)
        command = shell_prefix + cmd_split
    else:
        command = ["bash", "-c", f"{cmd}"]

    log.info("execute command: %s", cmd)

    popen_obj = subprocess.Popen(
        command, cwd=working_dir, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    while popen_obj.poll() is None:
        line = popen_obj.stdout.readline().strip()
        if line:
            log.info(line.decode("utf8", "ignore"))
    if not popen_obj.returncode:
        log.info("Executed Successfully! About:%s: %s\n", working_dir, cmd)
    else:
        log.info("\n")
        raise Exception(f"Command return code {popen_obj.returncode}")


def parse_args():
    parser = argparse.ArgumentParser(description='this script is for file cms')
    parser.add_argument('--result_path', '-r', required=True, help='this path for cms root or pkg_path')
    parser.add_argument('--pkg_path', '-p', help='pkg_name for this cms')
    args = parser.parse_args()
    return args


def cms_prepare(file_path, package_path):
    """返回CMS_ROOT和签名后打成包的路径"""
    file_path = Path(file_path)
    if file_path.is_dir():
        return str(file_path), str(package_path)
    if file_path.is_file():
        file_name = file_path.name.rsplit(".", 1)[0]  # str

        cms_root = Path(f'{WORKSPACE}/ws_cms_{file_name}')
        if cms_root.exists():
            shutil.rmtree(str(cms_root))

        cms_root.mkdir(parents=True, exist_ok=True)
        cmd = ""
        if str(file_path).endswith(".zip"):
            # zip解压
            cmd = f'7z x -y "{file_path}" -o"{cms_root}"'
        if str(file_path).endswith(".tar.gz") or str(file_path).endswith(".tgz"):
            # gzip和tar解压
            cmd = f'7z x -y "{file_path}" -so | 7z x -y -si -ttar -o"{cms_root}"'
        execute_command(cmd)

        if package_path is None:
            package_path = str(file_path)
        return str(cms_root), str(package_path)


def sign_sha256file(sha256sync_file):
    """签上CMS"""
    stat_flag = stat.S_IWUSR | stat.S_IRUSR
    common_json = os.path.join(WORKSPACE, "Build", "conf", "COMMON.json")
    with os.fdopen(os.open(common_json, os.O_RDWR, stat_flag), "r") as foo:
        conf_dict = json.loads(foo.read())

    sha256sync_file_dir = Path(sha256sync_file).parent
    sha256sync_name = Path(sha256sync_file).name
    signxml_path = Path(f"{WORKSPACE}/sign_conf.xml")

    # 兼容jenkins签名
    if os.getenv("CLOUD_BUILD2_URL") is None:
        sign_proxy = conf_dict["SIGN_PROXY_JENKINS"]
    else:
        sign_proxy = conf_dict["SIGN_PROXY_CLOUDBUILD"]

    signxml = f"""
<signtasks>
    <signtask name="sign_cms">
    <alias>CMS_Computing_RSA2048_CN_20220810_Huawei</alias>
    <file>{sha256sync_file}</file>
    <crlfile>{sha256sync_file_dir}{s}{sha256sync_name}.crl</crlfile>
    <hashtype>2</hashtype>
    <proxylist>{sign_proxy}</proxylist>
    <signaturestandard>5</signaturestandard>
    <productlineid>049944</productlineid>
    <versionid>{conf_dict["SIGN_VERSIONID"]}</versionid>
    </signtask>
</signtasks>
"""
    signxml_element = ET.fromstring(signxml)
    tree = ET.ElementTree(signxml_element)
    tree.write(str(signxml_path), encoding="utf-8", xml_declaration=True)
    # 执行签名
    execute_command(f'java -jar signature.jar "{signxml_path}"', SIGN_PLUGIN_HOME)


def compress_cmsroot(cms_root, package_path):
    """压缩到指定位置"""
    cmd = ""
    if Path(package_path).exists():
        Path(package_path).unlink()

    if package_path.endswith(".zip"):
        # zip压缩
        cmd = f'7z a -tzip "{package_path}" *'
    if package_path.endswith(".tar.gz") or package_path.endswith(".tgz"):
        # gzip压缩和tar归档
        p = Path(package_path)
        tar_path = p.stem.split(".", 1)[0]
        cmd = f'7z a -ttar "{tar_path}.tar" * -so | 7z a -tgzip "{package_path}" -si'
    execute_command(cmd, cms_root)


def encrypt(fpath: str, algorithm: str) -> str:
    with open(fpath, 'rb') as f:
        return hashlib.new(algorithm, f.read()).hexdigest()


def sha256sum_sync(cms_root) -> str:
    """遍历每个文件生成sha256sum_sync文件"""
    p = Path(cms_root)
    f_sha256sum = Path(f"{cms_root}/sha256sum_sync")
    with open(str(f_sha256sum), 'w+') as f_obj:
        for f_path in p.rglob("*"):
            if str(f_path) == str(f_sha256sum) or ".git" in str(f_path):
                continue
            if f_path.is_file():
                sha256_value = encrypt(str(f_path), "sha256")
                f_rela_path = str(f_path).replace(str(p) + s, "")
                f_obj.write(f"{f_rela_path} {sha256_value}\n")
    return str(f_sha256sum)


if __name__ == "__main__":
    arg_dict = parse_args()
    # 获取传入2参数，并预处理
    result_path = Path(arg_dict.result_path).absolute()
    if arg_dict.pkg_path is not None:
        pkg_path = Path(arg_dict.pkg_path).absolute()
    else:
        pkg_path = arg_dict.pkg_path

    # 在当前目录中匹配给定的模式
    for ph in result_path.parent.glob(str(result_path.name)):
        cms_root_dir, pkg_path1 = cms_prepare(ph, pkg_path)  # 准备cms签名根目录(含解压)
        sha256sync_path = sha256sum_sync(cms_root_dir)  # sha256_sync文件生成
        sign_sha256file(sha256sync_path)  # 给sha256_sync签名
        compress_cmsroot(cms_root_dir, pkg_path1)  # 打压缩
