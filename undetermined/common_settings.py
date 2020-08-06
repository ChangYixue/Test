#!/usr/bin/env python
# -*- coding:utf-8 -*-
from common.run_method import RunMethod
from common.read_info import ReadYaml
from common.get_log import get_log
import json


class CommonSettings(object):
    def __init__(self):
        self.run = RunMethod()
        self.ry = ReadYaml()
        self.logger = get_log()

    # 账户基本信息
    def account(self, api_name):
        try:
            method = self.ry.get_method(api_name)
            url = self.ry.get_url(api_name)
            data = None
            headers = self.ry.get_headers(api_name)
            response = self.run.run_main(method, url, data, headers)

            # print("===================== 账户基本信息的Response Body ====================")
            # print(json.dumps(response, ensure_ascii=False, sort_keys=False, indent=2))
            return response
        except Exception as e:
            self.logger.info("接口访问异常, %s" % e)

    # 账户菜单配置
    def configs(self, api_name):
        try:
            method = self.ry.get_method(api_name)
            url = self.ry.get_url(api_name)
            data = None
            headers = self.ry.get_headers(api_name)
            response = self.run.run_main(method, url, data, headers)

            # print("===================== 账户菜单配置的Response Body ====================")
            # print(json.dumps(response, ensure_ascii=False, sort_keys=False, indent=2))
            return response
        except Exception as e:
            self.logger.info("接口访问异常， %s" % e)

    # 默认货币列表
    def currencies(self, api_name):
        try:
            method = self.ry.get_method(api_name)
            url = self.ry.get_url(api_name)
            data = None
            headers = self.ry.get_headers(api_name)
            response = self.run.run_main(method, url, data, headers)

            # print("===================== 默认货币列表的Response Body ====================")
            # print(json.dumps(response, ensure_ascii=False, sort_keys=False, indent=2))
            return response
        except Exception as e:
            self.logger.info("接口访问异常， %s" % e)

    # 获取设备列表
    def list_device(self, api_name):
        try:
            method = self.ry.get_method(api_name)
            url = self.ry.get_url(api_name)
            data = None
            headers = self.ry.get_headers(api_name)
            response = self.run.run_main(method, url, data, headers)

            # print("===================== 设备列表的Response Body ====================")
            # print(json.dumps(response, ensure_ascii=False, sort_keys=False, indent=2))
            return response
        except Exception as e:
            self.logger.info("接口访问异常， %s" % e)

    # 获取地址簿列表
    def contact_list(self, api_name):
        try:
            method = self.ry.get_method(api_name)
            url = self.ry.get_url(api_name)
            data = None
            headers = self.ry.get_headers(api_name)
            response = self.run.run_main(method, url, data, headers)

            # print("===================== 地址簿列表的Response Body ====================")
            # print(json.dumps(response, ensure_ascii=False, sort_keys=False, indent=2))
            return response
        except Exception as e:
            self.logger.info("接口访问异常， %s" % e)


if __name__ == "__main__":
    cs = CommonSettings()
    # cs.list_device("list_device")
    # cs.contact_list("contact_list")
    # cs.account("account")
    # cs.configs("configs")
    cs.currencies("currencies")