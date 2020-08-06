#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import re
import yaml
import lib
import urllib
from urllib.parse import unquote
# read txt create TestCase info yml


def get_request_info(method='get', curl=''):
    assert len(curl) > 0, 'curl lenth <= 0'
    request_dic = {'method': method}

    # get url
    other, url = curl.split(' --data ')
    url = url.strip(''' ' ''')
    request_dic['url'] = url
    # get name
    name_flag = True
    name = url.split('/')[-2]

    # get data
    data_dic = {}

    request_dic['data'] = None

    if method == 'post':

        other, data = re.split(r'--data-binary', other)
        # other, data = other.split(' --data\ ')
        data_list = eval(data).split('&')

        for data in data_list:
            if '=' in data:
                data = unquote(data)
                key, value = data.split('=')
                data_dic[key] = value
            else:
                data_dic = json.loads(data)

        request_dic['data'] = data_dic

    # get headers
    headers_dic = {}
    headers = other.split(' -H ')[1:]

    for para in headers:
        para = eval(para)
        para = unquote(para, encoding='utf-8')
        key, value = para.split(': ')
        headers_dic[key] = value
    request_dic['headers'] = headers_dic

    return name, request_dic


def create_config():

    config_dic = {}

    with open('{path}{filename}.txt'.format(path=lib.CONFIG_PATH, filename=lib.FILENAME), 'r') as txt:
        for line in txt.readlines():
            line = line.strip()

            if len(line) <= 0:
                continue

            method = 'post' if '--data-binary'in line else 'get'
            req_name, req_info = get_request_info(method=method, curl=line)

            if req_name in config_dic.keys():
                key_list = config_dic.keys()

                rule = re.compile('.*{name}.*'.format(name=req_name))
                count = list(filter(rule.match, key_list)).__len__()
                # key 重复处理
                req_name = req_name+'_'+str(count)
                config_dic[req_name] = req_info

            config_dic[req_name] = req_info
        config = yaml.dump(config_dic, allow_unicode=True)

        with open('{path}{filename}Config.yml'.format(path=lib.CONFIG_PATH, filename=lib.FILENAME), 'w+', encoding='utf-8') as j:
            j.write(config)


if __name__ == "__main__":
    create_config()