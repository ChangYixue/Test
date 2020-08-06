#!/usr/bin/env python
# -*- coding:utf-8 -*-
from API.all_api import AllApi
import pytest
from common.get_log import get_log
logger = get_log()


# 财富模块的测试用例
@pytest.mark.usefixtures("init_token")
class TestFinancialInvest(object):
    @pytest.fixture(scope="class")
    def init_financial(self):
        logger.info("\n ==============================【财富】测试用例开始 ==============================")
        all_request = AllApi()
        return all_request

    # 【财富】财富产品列表
    @pytest.mark.parametrize("api_name", ['financial_list_products'])
    def test_list_product(self, api_name, init_financial):
        print("\n 用例名称：财富产品列表 \n")
        res = init_financial.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']

    # 【财富】财富产品详情
    @pytest.mark.parametrize("api_name", ['product_detail'])
    def test_product_detail(self, api_name, init_financial):
        print("\n 用例名称：财富产品详情 \n")
        res = init_financial.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']

    # 【财富】财富产品类型
    @pytest.mark.parametrize("api_name", ['list_products_type'])
    def test_list_products_type(self, api_name, init_financial):
        print("\n 用例名称：财富产品类型 \n")
        res = init_financial.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']

    # 【财富】我的财富列表
    @pytest.mark.parametrize("api_name", ['invested_products'])
    def test_invested_products(self, api_name, init_financial):
        print("\n 用例名称：我的财富列表 \n")
        res = init_financial.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']

    # 【财富】财富交易记录列表
    @pytest.mark.parametrize("api_name", ['records_list'])
    def test_records_list(self, api_name, init_financial):
        print("\n 用例名称：财富交易记录列表 \n")
        res = init_financial.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']

    # 【财富】币计划01-购买活期币计划
    # 备注：sandbox上没有可买的活期币计划
    @pytest.mark.skip(reason="sandbox上没有可买的活期币计划")
    @pytest.mark.parametrize("api_name", ["financial_invest"])
    def test_financial_invest_01(self, api_name, init_financial):
        print("\n 用例名称：购买活期币计划 \n")
        res = init_financial.send_request(api_name)
        assert res['success'] is False, "success的值为: %s" % res['success']

    # 【财富】币计划02-购买定期币计划
    @pytest.mark.skip(reason="sandbox上没有可买的定期币计划")
    @pytest.mark.parametrize("api_name", ["financial_invest_1"])
    def test_financial_invest_02(self, api_name, init_financial):
        print("\n 用例名称：购买定期币计划 \n")
        res = init_financial.send_request(api_name)
        assert res['success'] is False, "success的值为: %s" % res['success']

    # 【财富】兑换-支持的兑换币种对
    @pytest.mark.parametrize("api_name", ['coin_pairs'])
    def test_coin_pairs(self, api_name, init_financial):
        print("\n 用例名称：兑换-支持的兑换币种对 \n")
        res = init_financial.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']

    # 【财富】兑换-获取限额
    @pytest.mark.parametrize("api_name", ['pre_trade'])
    def test_pre_trade(self, api_name, init_financial):
        print("\n 用例名称：兑换-获取限额 \n")
        res = init_financial.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']

    # 【财富】兑换-获取交易限额
    @pytest.mark.parametrize("api_name", ['trade_info'])
    def test_trade_info(self, api_name, init_financial):
        print("\n 用例名称：兑换-获取交易限额 \n")
        res = init_financial.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']

    # 【财富】兑换-获取报价
    @pytest.mark.parametrize("api_name", ['exchange_quote'])
    def test_exchange_quote(self, api_name, init_financial):
        print("\n 用例名称：兑换-获取报价 \n")
        res = init_financial.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']

    # 【财富】兑换-确认交易
    @pytest.mark.skip(reason="quote需要从exchange_quote接口的返回值中获取")
    @pytest.mark.parametrize("api_name", ['exchange_trade'])
    def test_exchange_trade(self, api_name, init_financial):
        print("\n 用例名称：确认交易 \n")
        res = init_financial.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']

    # 【财富】兑换-获取闪兑记录
    @pytest.mark.parametrize("api_name", ['exchange_activities'])
    def test_exchange_activities(self, api_name, init_financial):
        print("\n 用例名称：兑换-获取闪兑记录 \n")
        res = init_financial.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']

    # 【囤币】囤币基本信息
    @pytest.mark.parametrize("api_name", ['tripple_main_info'])
    def test_tripple_main_info(self, api_name, init_financial):
        print("\n 用例名称：囤币基本信息 \n")
        res = init_financial.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']

    # 【囤币】囤币订单详情页
    @pytest.mark.parametrize("api_name", ['tripple_order_info'])
    def test_tripple_order_info(self, api_name, init_financial):
        print("\n 用例名称：囤币订单详情页 \n")
        res = init_financial.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']


if __name__ == "__main__":
    # pytest.main(['-v', 'test_financial.py', '-m=test'])
    # pytest.main(['-v', 'test_financial_invest.py', '--html=report/financial_invest_report.html'])
    # 运行所有测试用例文件-多线程（暂未成功）
    # pytest.main(['-v', '--html=report/all_report.html', '--self-contained-html', '--workers=1', '--tests-per-worker=1'])
    # 运行所有测试用例文件-单线程
    pytest.main(['-v', '--html=report/all_report.html', '--self-contained-html'])
