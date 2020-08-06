#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import base
from common.read_info import ReadYaml
from common.run_method import RunMethod
from common.get_log import get_log


class RewardsFinancial(object):
    def __init__(self):
        self.run = RunMethod()
        self.ry = ReadYaml()
        self.logger = get_log()

    # 财富产品列表
    def list_product(self, api_name):
        try:
            method = self.ry.get_method(api_name)
            url = self.ry.get_url(api_name)
            data = None
            headers = self.ry.get_headers(api_name)

            response = self.run.run_main(method, url, data, headers)

            # print("===================== 财富产品列表的Response Body ====================")
            # print(response)
            return response
        except Exception as e:
            self.logger.info("接口访问异常， %s" % e)

    # 我的财富列表
    def invested_products(self, api_name):
        try:
            method = self.ry.get_method(api_name)
            url = self.ry.get_url(api_name)
            data = None
            headers = self.ry.get_headers(api_name)

            response = self.run.run_main(method, url, data, headers)

            # print("===================== 我的财富列表的Response Body ====================")
            # print(response)
            return response
        except Exception as e:
            self.logger.info("接口访问异常， %s" % e)

    # 定期/活期币计划
    def invest_api(self, api_name):
        try:
            method = self.ry.get_method(api_name)
            url = self.ry.get_url(api_name)
            data = self.ry.get_data(api_name)
            headers = self.ry.get_headers(api_name)

            response = self.run.run_main(method, url, data, headers)

            # print("===================== 定期/活期币计划接口的Response Body ====================")
            # print(response)
            return response
        except Exception as e:
            self.logger.info("接口访问异常， %s" % e)


if __name__ == "__main__":
    # login_api("login")
    rf = RewardsFinancial()
    # rf.invest_api("financial_invest")
    # rf.list_product("financial_list_products")
    rf.invested_products("invested_products")


