"""
控制每次并发线程的数量，引入线程池
"""
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor


def allmain(repo):
    print('开始执行任务', repo)
    yellow_url = 'https://github.alibaba.com/api/v4/projects/'

    # xxxxxxxxxxxxx token
    header = {'PRIVATE-TOKEN': "xxxxxxxxx"}

    project_id = str(repo)
    url = yellow_url + project_id + "/repository/ref"
    # 关闭告警
    requests.packages.urllib3.disable_warnings()
    # urllib3.disable_warnings()
    # logging.captureWarnings(True)
    # 访问API
    response = requests.get(url, headers=header, verify=False)
    repository_branches_result = json.loads(response.content)
    repo_branches = repository_branches_result["branches"]
    print(repo_branches)

    time.sleep(5)


pool = ThreadPoolExecutor(10)

allrepo = {
    123: "ArrayUpgrade",
    124: "CliDK",
    125: "CollectDeviceArchives",
    126: "DeviceCabelDetect",
    127: "DiagnoseWeb",
}
for i in allrepo:
    pool.submit(allmain, i)

print("执行中....")
pool.shutdown(True) # 如果是想等所有任务完成，再关闭线程池，则设置pool.shutdown(wait=True)
print("继续往下走")
