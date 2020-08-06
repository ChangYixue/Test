#!/usr/bin/env python
# -*- coding:utf-8 -*-
from common.run_method import RunMethod
from common.read_info import ReadYaml
from common.get_log import get_log
import json


class Asset(object):
    def __init__(self):
        self.run = RunMethod()
        self.ry = ReadYaml()
        self.logger = get_log()

    # 资产列表
    def asset_main(self, api_name):
        try:
            method = self.ry.get_method(api_name)
            url = self.ry.get_url(api_name)
            headers = self.ry.get_headers(api_name)

            response = self.run.run_main(method, url, None, headers)
            # print("\n ===================== 资产列表接口的Response Body ====================")
            # print(response)
            return response
        except Exception as e:
            self.logger.info("接口访问异常，%s" % e)
            # self.logger.info(e)

    # BTC基本信息
    def coin_info(self, api_name):
        try:
            method = self.ry.get_method(api_name)
            url = self.ry.get_url(api_name)
            headers = self.ry.get_headers(api_name)

            response = self.run.run_main(method, url, None, headers)
            # print("\n ===================== BTC基本信息接口的Response Body ====================")
            # print(response)
            return response
        except Exception as e:
            self.logger.info("接口访问异常, %s " % e)

    # BTC的所有列表
    def all_activities(self, api_name):
        try:
            method = self.ry.get_method(api_name)
            url = self.ry.get_url(api_name)
            headers = self.ry.get_headers(api_name)

            response = self.run.run_main(method, url, None, headers)
            print("\n ===================== BTC的所有列表接口的Response Body ====================")
            print(json.dumps(response, ensure_ascii=False, sort_keys=False, indent=2))
            return response
        except Exception as e:
            self.logger.info("接口访问异常, %s " % e)

    # BTC的发送列表
    def send_activities(self, api_name):
        try:
            method = self.ry.get_method(api_name)
            url = self.ry.get_url(api_name)
            headers = self.ry.get_headers(api_name)

            response = self.run.run_main(method, url, None, headers)
            print("\n ===================== BTC的发送列表接口的Response Body ====================")
            print(json.dumps(response, ensure_ascii=False, sort_keys=False, indent=2))
            return response
        except Exception as e:
            self.logger.info("接口访问异常, %s " % e)

    # BTC的接收列表
    def receive_activities(self, api_name):
        try:
            method = self.ry.get_method(api_name)
            url = self.ry.get_url(api_name)
            headers = self.ry.get_headers(api_name)

            response = self.run.run_main(method, url, None, headers)
            print("\n ===================== BTC的接收列表接口的Response Body ====================")
            print(json.dumps(response, ensure_ascii=False, sort_keys=False, indent=2))
            return response
        except Exception as e:
            self.logger.info("接口访问异常, %s " % e)


if __name__ == "__main__":
    # login_api("login")
    asset = Asset()
    # asset.asset_main("asset_main")
    # asset.coin_info("coin_info_BTC")
    # asset.all_activities("all_activities_BTC")
    # asset.send_activities("send_activities_BTC")
    asset.receive_activities("receive_activities_BTC")


