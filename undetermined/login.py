#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import base
from common.read_info import ReadYaml
from common.run_method import RunMethod
from common.deal_token import write_token
import json
from common.get_log import get_log
logger = get_log()


def login_api(api_name):
    try:
        run = RunMethod()
        ry = ReadYaml()

        url = ry.get_url(api_name)
        method = ry.get_method(api_name)
        headers = ry.get_headers(api_name)
        data = ry.get_data(api_name)
        # response = run.run_main(method, url, data, headers)
        response = run.run_main(method, url, data, headers)

        # 把token值写到配置文件access_token.yml中
        write_token(response)

        # print("===================== 登录接口的Response Body ====================")
        # print(json.dumps(response, ensure_ascii=False, sort_keys=False, indent=2))
        return response
    except Exception as e:
        logger.info("接口访问异常， %s" % e)


if __name__ == "__main__":
    login_api("login")