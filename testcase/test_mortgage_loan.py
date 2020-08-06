#!/usr/bin/env python
# -*- coding:utf-8 -*-
from API.all_api import AllApi
import pytest
from common.get_log import get_log
logger = get_log()


# 借贷模块的测试用例
@pytest.mark.usefixtures("init_token")
class TestMortgageLoan(object):
    @pytest.fixture(scope="class")
    def init_mortgage_loan(self):
        logger.info("\n ==============================【借贷】测试用例开始 ==============================")
        all_request = AllApi()
        return all_request

    # 【借贷】抵押借贷主页面
    @pytest.mark.parametrize("api_name", ['mortgage_loan_main'])
    def test_mortgage_loan_main(self, api_name, init_mortgage_loan):
        print("\n 用例名称：抵押借贷主页面 \n")
        res = init_mortgage_loan.send_request(api_name)
        assert res['success'] is True, "success的值为：%s" % res['success']

    # 【借贷】全部列表
    @pytest.mark.parametrize("api_name", ['loan_list_all'])
    def test_loan_list_all(self, api_name, init_mortgage_loan):
        print("\n 用例名称：全部列表 \n")
        res = init_mortgage_loan.send_request(api_name)
        assert res['success'] is True, "success的值为：%s" % res['success']

    # 【借贷】未完成列表
    @pytest.mark.parametrize("api_name", ['loan_list_in_progress'])
    def test_loan_list_in_progress(self, api_name, init_mortgage_loan):
        print("\n 用例名称：未完成列表 \n")
        res = init_mortgage_loan.send_request(api_name)
        assert res['success'] is True, "success的值为：%s" % res['success']

    # 【借贷】已完成列表
    @pytest.mark.parametrize("api_name", ['loan_list_finished'])
    def test_loan_list_finished(self, api_name, init_mortgage_loan):
        print("\n 用例名称：已完成列表 \n")
        res = init_mortgage_loan.send_request(api_name)
        assert res['success'] is True, "success的值为：%s" % res['success']

    # 【借贷】借款和质押币种的汇率和质押币种余额
    @pytest.mark.parametrize("api_name", ['loan_rate_balance'])
    def test_loan_rate_balance(self, api_name, init_mortgage_loan):
        print("\n 用例名称：借款和质押币种的汇率和质押币种余额 \n")
        res = init_mortgage_loan.send_request(api_name)
        assert res['success'] is True, "success的值为：%s" % res['success']

    # 【借贷】借贷页面详情
    @pytest.mark.parametrize("api_name", ['loan_lend_detail'])
    def test_loan_lend_detail(self, api_name, init_mortgage_loan):
        print("\n 用例名称：借贷页面详情 \n")
        res = init_mortgage_loan.send_request(api_name)
        assert res['success'] is True, "success的值为：%s" % res['success']

    # 【借贷】发送借贷请求
    @pytest.mark.skip(reason="发送借贷请求：频繁发送接口会导致订单过多")
    @pytest.mark.parametrize("api_name", ['loan_lend'])
    def test_loan_lend(self, api_name, init_mortgage_loan):
        print("\n 用例名称：发送借贷请求 \n")
        res = init_mortgage_loan.send_request(api_name)
        assert res['success'] is True, "success的值为：%s" % res['success']

    # 【借贷】自动还款
    @pytest.mark.parametrize("api_name", ['loan_auto_payback'])
    def test_loan_auto_payback(self, api_name, init_mortgage_loan):
        print("\n 用例名称：自动还款 \n")
        res = init_mortgage_loan.send_request(api_name)
        assert res['success'] is True, "success的值为：%s" % res['success']

    # 【借贷】自动补仓
    @pytest.mark.parametrize("api_name", ['loan_auto_append'])
    def test_loan_auto_append(self, api_name, init_mortgage_loan):
        print("\n 用例名称：自动补仓 \n")
        res = init_mortgage_loan.send_request(api_name)
        assert res['success'] is True, "success的值为：%s" % res['success']

    # 【借贷】订单详情页
    @pytest.mark.parametrize("api_name", ['loan_order_info'])
    def test_loan_order_info(self, api_name, init_mortgage_loan):
        print("\n 用例名称：订单详情页 \n")
        res = init_mortgage_loan.send_request(api_name)
        assert res['success'] is True, "success的值为：%s" % res['success']


if __name__ == "__main__":
    pytest.main(['-v', 'test_mortgage_loan.py'])

