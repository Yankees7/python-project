#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright Huawei Technologies Co., Ltd. 2023-2050. All rights reserved.
"""
调用github-api完成一些批量重复性的操作
"""

import json
import logging as log
import requests
from typing import Dict, List

requests.packages.urllib3.disable_warnings()  # 关闭ssl证书告警
LOG_FORMAT = "%(asctime)s %(levelname)s %(funcName)s %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
log.basicConfig(level=log.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)

class Github:
    private_token = "afdsafdafd"
    prefix = "https://github.com"
    headers = {"private_token":f"{private_token}"}
    
    @staticmethod
    def get_project_name(projectid: int) -> str:
        """返回仓库名"""
        postfix = f"/projects/{projectid}"
        api_url = Github.prefix + postfix
        r = requests.get(api_url, headers=Github.headers, verify=False)
        r_obj = json.loads(r.content.decode())
        return r_obj["name"]

    @staticmethod
    def delete_branch(projectid: int, branch: str, PrintLog: bool = False) -> None:
        """删除仓库的分支"""
        postfix = f"/projects/{projectid}/repository/branches/{branch}"
        api_url = Github.prefix + postfix
        r = requests.delete(api_url, headers=Github.headers, verify=False)
        r_obj = json.loads(r.content.decode())
        if PrintLog is True:
            if not r.ok:
                log.error(
                    "Failure: ProjectName:%s, branch:%s response: \n%s",
                    Github.get_project_name(projectid),
                    branch,
                    r_obj,
                )

<<<<<<< HEAD

if __name__ == "__main__":
    ...
=======
    @staticmethod
    def get_all_projectid(top_groupid: str) -> List[int]:
        """递归获取组织下所有项目"""
        global groups_list
        global projects_list
        groups_list = []
        projects_list = []
        # 先获取所有子组织
        Github.app_list_all_groups(top_groupid)
        try:
            groups_list.remove(484527) # 移除不要的
        except Exception as e:
            log.ifo(e)
        # 根据组织获取项目
        for g in groups_list:
            getrepo_url = Github.prefix + f"/groups/{g}/projects?perge=1&per_page=100"
            r = requests.get(getrepo_url,headers=Github.headers,verify=False)
            if len(r.text) != 0:
                r_obj = json.loads(r.content.decode())
                for p in r_obj:
                    projects_list.append(p["id"])
        return projects_list


if __name__ == "__main__":
    ...
    # extend追加元素1,2，append只能一个一个加
    # list.extend([1,2])
>>>>>>> 8e1f0ef7eb7ac181dca39d39992fe37c81a36252
