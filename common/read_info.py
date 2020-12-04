#!/usr/bin/env python
# -*- coding:utf-8 -*-
from common import base
import yaml
from common.deal_token import read_token
import os
import time


class ReadYaml(object):
    def read_yml(self):
        # 获取配置文件路径
        curPath = os.path.abspath(os.path.dirname(__file__))
        yamlPath = os.path.abspath(os.path.dirname(curPath) + os.path.sep + "configs/api_config.yml")
        # yamlPath = os.path.dirname(os.path.abspath('.'))+'/data/config.yml'
        # print(yamlPath)

        f = open(yamlPath, 'r', encoding='utf-8')

        content = f.read()
        contents = yaml.load(content, Loader=yaml.FullLoader)
        '''
        print("文件中所有内容：", contents)
        print("登录接口内容：", contents['login'])
        '''
        return contents

    def get_url(self, api_name):
        content = self.read_yml()
        new_url = content['host']+content[api_name]['url']
        # print("请求地址： ", new_url)
        return new_url

    def get_method(self, api_name):
        content = self.read_yml()
        # print("请求方式： ", content[api_name]['method'])
        return content[api_name]['method']

    def get_data(self, api_name):
        content = self.read_yml()
        # print("请求数据： ", content[api_name]['data'])
        return content[api_name]['data']

    def get_headers(self, api_name):
        content = self.read_yml()
        # print("请求头： ", content[api_name]['headers'])
        if api_name == "login":
            return content[api_name]['headers']
        else:
            # auth = content[api_name]['headers']['Authorization']+' '+read_token()
            # content[api_name]['headers']['Authorization'] = auth
            return content[api_name]['headers']

    # 获取响应结果的预期结果
    def get_expected(self, api_name):
        content = self.read_yml()
        expected = content[api_name]['expected']
        # print(expected, type(expected), expected["success"], expected["decimal"])
        return expected

    def get_time(self):
        # 以毫秒为单位的时间戳
        get_now_milli_time = int(time.time() * 1000)
        print(get_now_milli_time)


if __name__ == "__main__":
    # read_yml()
    ry = ReadYaml()
    # ry.is_login("login_prod")
    ry.get_time()
