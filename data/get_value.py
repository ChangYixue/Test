#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import requests
import json,re


def fund_test():
    requests.packages.urllib3.disable_warnings()

    # 161005 富国天惠
    # 以毫秒为单位的当前时间的时间戳
    get_now_milli_time = str(int(time.time() * 1000))

    jsl_url = "https://www.jisilu.cn/data/lof/detail_fund/?___jsl=LST___t="+ get_now_milli_time # jsl的url
    # jsl发送数据

    id = [163417, 161005]  # 多个产品id
    # print("id是：", id[0])
    jsl_res = []
    fund_names = []
    current_prices = []
    fund_navs = []
    jsl_estimate_values = []
    jsl_discount_rts = []

    for i in range(len(id)):
        jsl_data = {
            "is_search": 1,
            "fund_id": id[i],  # 不同产品只有次参数不同
            "fund_type": "stock",
            "rp": 50,
            "page": 1,
        }
        jsl_response = requests.post(url=jsl_url, headers=None, data=jsl_data, verify=False)  # jsl的返回数据
        jsl_response = jsl_response.json()

        jsl_res.append(jsl_response)

        fund_name = jsl_res[i]["rows"][0]['cell']['fund_nm']  # 产品名称
        fund_names.append(fund_name)

        current_price = jsl_res[i]["rows"][0]['cell']['price']  # 当前价格
        current_prices.append(current_price)

        fund_nav = jsl_res[i]["rows"][0]['cell']['fund_nav']  # 昨日净值
        fund_navs.append(fund_nav)

        jsl_estimate_value = jsl_res[i]["rows"][0]['cell']['estimate_value']  # jsl估值
        jsl_estimate_values.append(jsl_estimate_value)

        jsl_discount_rt = jsl_res[i]["rows"][0]['cell']['discount_rt']  # jsl溢价率
        jsl_discount_rts.append(jsl_discount_rt)

        print(type(fund_name), fund_names[i],current_prices[i],fund_navs[i],jsl_estimate_values[i], jsl_discount_rts[i])
        # jsl_res = json.dumps(jsl_response.json(), ensure_ascii=False, sort_keys=False, indent=2)
    # jsl_res = jsl_res[0]  # 临时

    tt_url = "http://fundgz.1234567.com.cn/js/163417.js?rt=" + get_now_milli_time  # tt的url
    # print(tt_url)

    tt_response = requests.get(tt_url)  # tt的返回数据
    tt_res = tt_response.text[:-1]  # 去除最后一个字符的tt的返回数据
    # print(tt_response, tt_res, type(tt_res))
    j = json.loads(re.findall(r'^\w+\((.*)\)$', tt_res)[0])
    # print(type(j), j,j['name'], j['gsz'], type(j['gsz']))

    # ============ 表格中需要的数据 ============

    current_time = time.strftime("%Y-%m-%d", time.localtime())  # 当前日期
    # print(current_time)


    # fund_name = jsl_res["rows"][0]['cell']['fund_nm']  # 产品名称
    # current_price = jsl_res["rows"][0]['cell']['price']  # 当前价格
    # fund_nav = jsl_res["rows"][0]['cell']['fund_nav']  # 昨日净值
    # jsl_estimate_value = jsl_res["rows"][0]['cell']['estimate_value']  # jsl估值
    # jsl_discount_rt = jsl_res["rows"][0]['cell']['discount_rt']  # jsl溢价率

    tt_discount_rt = (float(current_prices[0]) - float(j['gsz'])) / float(j['gsz']) * 100  # 天天溢价率=(现价-天天估值）/天天估值*100%
    tt_discount_rt = round(tt_discount_rt, 2)  # 天天溢价率保留两位小数
    # print(tt_discount_rt)

    render = {"tt_res": 1, 'current_price': current_prices[0], "fund_nav": fund_navs[0], "jsl_estimate_value": jsl_estimate_values[0],"jsl_discount_rt": jsl_discount_rts[0],
              "current_time": current_time, "fund_name": fund_names[0], "tt_data": 7,"tt_discount_rt": 8,}

    print(render)
    return render


if __name__ == "__main__":
    fund_test()
