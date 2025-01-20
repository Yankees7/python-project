#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright Tenxun Technologies Co., Ltd. 2023-2050. All rights reserved.
"""
jenkins构建时,上传源码、镜像信息、版本包签名

必要软件：
JAVA
PYTHON
SIGN_PLUGIN_HOME环境及环境变量
artget

使用方法：
python Build\script\jenkins_env_src_upload_cmc.py -s "/usr1/workspace/UltraPath" -e "aixenv,Aix_5.3.0.0_PowerPC_POWER5,X86,AIX" -p "Code\build\script\odm\result\OceanStor_AIX_ODM.zip" -r "UltraPath ODM"
-s 源码仓所在目录
-e 镜像信息,依次是: 镜像id,镜像名,架构,工程名
-p 构建结果包路径，可以是包路径或者是只含这包目录路径；
-r 远程仓库的归档路径
"""
import os
import sys
import stat
import json
import argparse
import subprocess
import shlex
import logging as log
import xml.etree.ElementTree as ET
from pathlib import Path
import configparser

log.basicConfig(level=log.INFO)
default_workspace = r"d:\workspace" if sys.platform == "win32" else "/usr1/workspace"
WORKSPACE = os.getenv("WORKSPACE", default_workspace)
SIGN_PLUGIN_HOME = os.getenv("SIGN_PLUGIN_HOME", os.getenv("SIGNATURE_HOME"))
s = os.sep
upbversion = os.getenv("UPBVERSION", "UltraPath 31.3.0.B105")


def execute_command(cmd: str, working_dir: str = WORKSPACE) -> None:
    """仅执行系统命令,无返回结果,有报错机制\n
    采用shlex.split适应windows空格路径,所以windows路径请用双引号引起来"""
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
    parser = argparse.ArgumentParser(description='this script is for jenkins')
    parser.add_argument('--src_dir', '-s', required=True, help='source code url')
    parser.add_argument('--env', '-e', required=True, help='env info')
    parser.add_argument('--pkg_path', '-p', required=True, help='package path')
    parser.add_argument('--cmc_path', '-r', required=True, help='package path')
    args = parser.parse_args()
    return args


def source_upload(source_dir):
    """制作源码信息上传CMC"""
    sourcecode_xml_path = Path(f"{WORKSPACE}/FOLLOW_CMC_ARTIFACT/SourceCode.xml")
    if not sourcecode_xml_path.parent.exists():
        sourcecode_xml_path.parent.mkdir(parents=True, exist_ok=True)

    # 获取CommitID和远程仓库地址
    current_id = execute_command("git rev-parse HEAD", source_dir)

    # 获取git_url
    conf_path = Path(f"{source_dir}/.git/config")
    config = configparser.ConfigParser()
    config.read(str(conf_path))
    git_url = config['remote "origin"']["url"]

    # 获取git分支
    try:
        branch = execute_command("git symbolic-ref --short HEAD", source_dir)
    except Exception:
        branch = "master"
    # 获取仓库名
    repo_name = Path(source_dir).name

    sourcecode_xml = f"""
<Results>
    <versionType>BVersion</versionType>
    <Offering>{offering}</Offering>
    <version>{upbversion}</version>
    <dependentSourceFiles>
            <fileidentify repoBase="{git_url}" branch="{branch}" revision="{current_id}" repoType="GIT" localpath="{repo_name}" />
    </dependentSourceFiles>
</Results>
"""
    sourcecode_element = ET.fromstring(sourcecode_xml)
    tree = ET.ElementTree(sourcecode_element)
    tree.write(str(sourcecode_xml_path), encoding="utf-8", xml_declaration=True)
    # upload
    execute_command(f'artget push -sc "{sourcecode_xml_path}"')


def env_upload(env_info):
    """制作镜像信息上传CMC"""
    env_xml_path = Path(f"{WORKSPACE}/FOLLOW_CMC_ARTIFACT/Env_image.xml")
    if not env_xml_path.parent.exists():
        env_xml_path.parent.mkdir(parents=True, exist_ok=True)

    # 解析env_info
    env_list = env_info.split(",")
    image_id = env_list[0]
    image_name = env_list[1]
    platform = env_list[2]
    project_name = env_list[3]

    env_xml = f"""
<project>
    <versionType>BVersion</versionType>
    <offering>{offering}</offering>
    <version>{upbversion}</version>
    <envImages>
         <image imageId="{image_id}" imageName="{image_name}" imageSource="ArtGet" commitId="NA" envConfigFilePath="NA" platform="{platform}" projectId="NA" projectName="{project_name}" />
   </envImages>
</project>
"""
    env_element = ET.fromstring(env_xml)
    tree = ET.ElementTree(env_element)
    tree.write(str(env_xml_path), encoding="utf-8", xml_declaration=True)
    # upload
    execute_command(f'artget push -ei "{env_xml_path}"')


def sign_hwp7s(package_path):
    """给包签名版本包p7s"""
    package_path = Path(f"{package_path}")
    if not package_path.parent.exists():
        package_path.parent.mkdir(parents=True, exist_ok=True)

    fileset_structure = f"""
        <fileset path="{package_path}">
            <include>**/*.zip</include>
            <include>**/*.tar.gz</include>
            <exclude>*/*.cms</exclude>
            <exclude>*/*.crl</exclude>
        </fileset>
"""
    singlefile_structure = f"""
        <file>{package_path}</file>
"""
    if package_path.is_dir():
        finally_structure = fileset_structure
    if package_path.is_file():
        finally_structure = singlefile_structure
    stat_flag = stat.S_IWUSR | stat.S_IRUSR
    common_json = os.path.join(WORKSPACE, "Build", "conf", "COMMON.json")
    with os.fdopen(os.open(common_json, os.O_RDWR, stat_flag), "r") as foo:
        conf_dict = json.loads(foo.read())

    signxml_path = Path(f"{WORKSPACE}/sign_conf.xml")
    # 兼容jenkins签名
    if os.getenv("CLOUD_BUILD2_URL") is None:
        sign_proxy = conf_dict["SIGN_PROXY_JENKINS"]
    else:
        sign_proxy = conf_dict["SIGN_PROXY_CLOUDBUILD"]

    signxml = f"""
<signtasks>
    <signtask name="hwp7s">
        <alias>CMS_G5_Test_Sign_RSA3072PSS_CN_20220505_HUAWEI</alias>
        <timestampalias>CMS_G5_Test_TSA_RSA3072PSS_CN_20220505_HUAWEI</timestampalias>
        {finally_structure}
        <hashtype>1</hashtype>
        <padmode>1</padmode>
        <proxylist>{sign_proxy}</proxylist>
        <signaturestandard>5</signaturestandard>
        <productlineid>049944</productlineid>
        <versionid>{conf_dict["SIGN_VERSIONID"]}</versionid>
        <crlfile>crldata.crl</crlfile>
    </signtask>
</signtasks>    
"""
    signxml_element = ET.fromstring(signxml)
    tree = ET.ElementTree(signxml_element)
    tree.write(str(signxml_path), encoding="utf-8", xml_declaration=True)
    # 执行签名
    execute_command(f'java -jar signature.jar "{signxml_path}"', SIGN_PLUGIN_HOME)


def upload_artifacts(package_path, remote_path):
    """上传签名后的包"""
    package_path = Path(package_path)
    upload_agent = str(package_path.parent)

    source_dir_structure = f"""
<source>{package_path.name}</source> 
"""
    source_file_structure = f"""
    <source>{package_path.name}</source>
    <source>{package_path.name}.hwp7s</source> 
"""

    if package_path.is_dir():
        source_structure = source_dir_structure
    if package_path.is_file():
        source_structure = source_file_structure

    # 上传CMC归档
    upload_xml = f"""
<project>
    <artifact>
        <versionType>BVersion</versionType>
        <repoType>Generic</repoType>
        <id>
            <offering>{offering}</offering>
            <version>{upbversion}</version>
        </id>
        <isClear>N</isClear>
        <copies>
            <copy>
                {source_structure}
                <dest>{remote_path}</dest>
            </copy>
        </copies>
    </artifact>
</project>
"""
    signxml_element = ET.fromstring(upload_xml)
    tree = ET.ElementTree(signxml_element)
    upload_xml_path = Path(f"{WORKSPACE}/upload_cmc.xml")
    tree.write(str(upload_xml_path), encoding="utf-8", xml_declaration=True)

    # 执行上传
    execute_command(f'artget push -d "{upload_xml_path}" -ap "{upload_agent}" ')


if __name__ == '__main__':
    if upbversion != "false":
        arg_dict = parse_args()
        # 传入参数预处理
        src_dir = str(Path(arg_dict.src_dir).absolute())
        pkg_path = str(Path(arg_dict.pkg_path).absolute())
        env_li = arg_dict.env
        cmc_path = arg_dict.cmc_path

        offering = " ".join(upbversion.split()[0:-1])
        source_upload(src_dir)
        env_upload(env_li)
        sign_hwp7s(pkg_path)
        upload_artifacts(pkg_path, cmc_path)
