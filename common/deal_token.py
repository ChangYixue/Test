#!/usr/bin/env python
# -*- coding:utf-8 -*-
from common import base
import os
import yaml
import json
from common.run_method import RunMethod
from common.get_log import get_log
logger = get_log()


# 把token值写到配置文件access_token.yml中
def write_token(res):
    curPath = os.path.abspath(os.path.dirname(__file__))
    yamlPath = os.path.abspath(os.path.dirname(curPath) + os.path.sep + "configs/access_token.yml")
    # yamlPath = os.path.dirname(os.path.abspath('.'))+'/data/access_token.yml'
    # res = json.loads(res)

    tokenValue = {
        'access_token': res["access_token"]
    }
    with open(yamlPath, 'w', encoding='utf-8') as f:
        yaml.dump(tokenValue, f)

    logger.info("\n token值已保存至配置文件中")


def read_token():
    curPath = os.path.abspath(os.path.dirname(__file__))
    path = os.path.abspath(os.path.dirname(curPath) + os.path.sep + "configs/access_token.yml")
    # path = os.path.dirname(os.path.abspath('.'))+'/data/access_token.yml'
    file = open(path)
    read = file.read()
    load = yaml.load(read, Loader=yaml.FullLoader)
    file.close()
    return load['access_token']


if __name__ == "__main__":
    run = RunMethod()
    url = "https://xxx/v1/login/"
    data = {
        "phone_country": "86",
        "phone_number": "12100766832",
        "password": "1234&qweR",
        "device_id": "FE6C89E6-1B18-43C3-B9B9-CA2D773D64D8",
        "device_name": "Iphone8plus",
        "device_pubkey": "3tVcBc1K0QmYnkwI7z7+s3ZL4kx0kYmEYERvMDZU/0k="
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic S01IeWFuMnF3SUY3RGI2eDhvdVNDQ0hrekVBUlRHbFE6aElhbU1ncnJZcVlOeEJxS2Z4Ykh2Uk9TZ0N0M1loc2o="
    }

    res = run.run_main("Post", url, data, headers)
    # print(res)
    response = json.loads(res)
    write_token(response)
    print("token的值： ", read_token())