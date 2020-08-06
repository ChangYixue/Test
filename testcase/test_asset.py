#!/usr/bin/env python
# -*- coding:utf-8 -*-
# fileName: test_asset.py
from API.all_api import AllApi
import pytest
from common.get_log import get_log
logger = get_log()


# 资产模块的测试用例
@pytest.mark.asset
@pytest.mark.usefixtures("init_token")
class TestAsset(object):
    @pytest.fixture(scope="class")
    def init_asset(self):
        logger.info("\n ==============================【资产】测试用例开始 ==============================")
        all_request = AllApi()
        return all_request

    @pytest.mark.test
    @pytest.mark.parametrize("api_name", ["asset_main"])
    def test_asset_main(self, api_name, init_asset):
        print("\n 用例名称：获取资产列表信息\n")
        res = init_asset.send_request(api_name)
        # 获取某接口下的预期返回结果
        expected = init_asset.get_expect(api_name)
        # 断言1：success的值为true
        # assert res['success'] is True, "success的值为: %s" % res['success']
        # assert res['status_code'] == expected['status_code'], "status_code的值为: %s" % res['status_code']
        assert res['success'] == expected['success'], "success的值为: %s" % res['success']
        # 断言2：coin的值等于"BTC"
        # assert res["result"]["wallets"][0]["coin"] == expected['coin'], "coin的值为：%s" % res["result"]["wallets"][0]["coin"]

    # @pytest.mark.test
    @pytest.mark.parametrize("api_name", ["coin_info_BTC"])
    def test_coin_info(self, api_name, init_asset):
        print("\n 用例名称：获取币种基本信息\n")
        res = init_asset.send_request(api_name)
        # 断言1：success的值为true
        assert res['success'] is True, "success的值为: %s" % res['success']
        # 断言2：coin的值等于"BTC"
        assert res['result']['wallets'][0]['coin'] == "BTC", "coin的值为: %s" % res['result']['wallets'][0]['coin']

    @pytest.mark.parametrize('api_name', ["message_list"])
    def test_message_list(self, api_name, init_asset):
        print("\n 用例名称：云端钱包公告列表 \n")
        res = init_asset.send_request(api_name)
        assert res["success"] is True, "success的值为: %s" % res['success']

    # 【资产】某币种的列表：全部、发送、接收、财富、闪电网络和借贷
    @pytest.mark.allLists
    @pytest.mark.parametrize('api_name', ['all_activities_BTC', 'send_activities_BTC', 'receive_activities_BTC', 'finance_activities_BTC', 'mortgage_activities_BTC'])
    def test_all_activities(self, api_name, init_asset):
        print("\n 用例名称： 资产记录列表（全部、发送、接收、财富、借贷） \n")
        res = init_asset.send_request(api_name)
        expected = init_asset.get_expect(api_name)
        assert res["success"] is True, "success的值为: %s" % res['success']
        assert res["result"]["wallet"]["display_code"] == expected["display_code"], "display_code的值为: %s" % res["result"]["wallet"]["display_code"]

    # 【资产】获取所有支持的币种
    @pytest.mark.parametrize("api_name", ['all_coins'])
    def test_all_coins(self, api_name, init_asset):
        print("\n 用例名称：获取所有支持的币种 \n")
        res = init_asset.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']

    # 【资产】获取发币信息和交易费
    @pytest.mark.parametrize("api_name", ['pre_send'])
    def test_pre_send(self, api_name, init_asset):
        print("\n 用例名称：获取发币信息和交易费 \n")
        res = init_asset.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']

    # 【资产】获取交易详情
    @pytest.mark.skip(reason="交易id需要未过时的id")
    @pytest.mark.parametrize("api_name", ['tx_info'])
    def test_tx_info(self, api_name, init_asset):
        print("\n 用例名称：获取交易详情 \n")
        res = init_asset.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']

    # 【资产】获取发币验证方法
    # @pytest.mark.skip(reason="预计会失败，但是也存在成功的情况")
    # @pytest.mark.test1
    @pytest.mark.parametrize("api_name", ['get_verify_methods_internal'])
    def test_get_verify_methods(self, api_name, init_asset):
        print("\n 用例名称：获取发币验证方法 \n")
        res = init_asset.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']

    # 【资产】发送发币请求-站内发币
    # 重要：请求该接口前必须先请求"获取发币验证方法"接口
    @pytest.mark.skip(reason="发币频繁可能会被风控拦截")
    @pytest.mark.parametrize("api_name", ['get_verify_methods_internal', 'send_internal'])
    def test_send(self, api_name, init_asset):
        print("\n 用例名称：发送发币请求 \n")
        res = init_asset.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']

    # 【资产】发送发币请求-站外发币
    # 重要：请求该接口前必须先请求"获取发币验证方法"接口
    @pytest.mark.skip(reason="发币频繁可能会被风控拦截")
    @pytest.mark.parametrize("api_name", ['get_verify_methods_external', 'send_external'])
    def test_send(self, api_name, init_asset):
        print("\n 用例名称：发送发币请求 \n")
        res = init_asset.send_request(api_name)
        assert res['success'] is True, "success的值为: %s" % res['success']


if __name__ == "__main__":
    # 若存在多个标记，则用or连接，形成一个测试集，比如'-m=assetList or test or allLists'
    pytest.main(['-s', 'test_asset.py', '-m=test'])
    # pytest.main(['-v', 'test_asset.py', '--html=report/asset_report.html', '--self-contained-html'])


