#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
from API.all_api import AllApi
from common.get_log import get_log
logger = get_log()


# 我的模块的测试用例
@pytest.mark.usefixtures("init_token")
class TestCommonSettings(object):
    @pytest.fixture(scope="class")
    def init_common_settings(self):
        logger.info("\n ==============================【我的】测试用例开始 ==============================")
        all_request = AllApi()
        return all_request

    # 【我的】账户基本信息
    @pytest.mark.parametrize("api_name", ["account"])
    def test_account(self, api_name, init_common_settings):
        print("\n 用例名称：账户基本信息 \n")
        res = init_common_settings.send_request(api_name)
        assert res["success"] is True, "success的值为：%s" % res["success"]
        assert res['result']['account']['account_id'] is not None, "account_id的值是：%s" % res['result']['account']['account_id']

    # 【我的】账户菜单配置
    @pytest.mark.parametrize("api_name", ["configs"])
    def test_configs(self, api_name, init_common_settings):
        print("\n 用例名称：账户菜单配置 \n")
        res = init_common_settings.send_request(api_name)
        assert res["success"] is True, "success的值为：%s" % res["success"]
        # assert res['result']['mortgage']is not None, "mortgage的值是：%s" % res['result']['mortgage']

    # 【我的】默认货币列表
    @pytest.mark.parametrize("api_name", ["currencies"])
    def test_currencies(self, api_name, init_common_settings):
        print("\n 用例名称：默认货币列表 \n")
        res = init_common_settings.send_request(api_name)
        assert res["success"] is True, "success的值为：%s" % res["success"]
        assert res['result']['currencies'][0]['code'] is not None, "code的值是：%s" % res['result']['currencies'][0]['code']

    # 【我的】人民币和各币种的比率
    @pytest.mark.parametrize("api_name", ["coin_rate"])
    def test_coin_rate(self, api_name, init_common_settings):
        print("\n 用例名称：人民币和各币种的比率 \n")
        res = init_common_settings.send_request(api_name)
        assert res["success"] is True, "success的值为：%s" % res["success"]

    # 【我的】kyc等级和限额
    @pytest.mark.parametrize("api_name", ["quota_coin"])
    def test_quota_coin(self, api_name, init_common_settings):
        print("\n 用例名称：kyc等级和限额 \n")
        res = init_common_settings.send_request(api_name)
        assert res["success"] is True, "success的值为：%s" % res["success"]

    # 【我的】设备列表
    @pytest.mark.parametrize("api_name", ["list_device"])
    def test_list_device(self, api_name, init_common_settings):
        print("\n 用例名称：设备列表 \n")
        res = init_common_settings.send_request(api_name)
        assert res["success"] is True, "success的值为：%s" % res["success"]
        assert res['result'][0]['device_name'] is not None, "device_name的值是：%s" % res['result'][0]['device_name']

    # 【我的】地址簿列表
    @pytest.mark.parametrize("api_name", ["contact_list"])
    def test_contact_list(self, api_name, init_common_settings):
        print("\n 用例名称：地址簿列表 \n")
        res = init_common_settings.send_request(api_name)
        assert res["success"] is True, "success的值为：%s" % res["success"]
        assert res['result'][0]['address_id'] is not None, "address_id的值是：%s" % res['result'][0]['address_id']

    # 【我的】地址簿-编辑/修改已有地址
    @pytest.mark.skip(reason="缺乏测试数据")
    @pytest.mark.parametrize("api_name", ["contact_edit"])
    def test_contact_edit(self, api_name, init_common_settings):
        print("\n 用例名称：地址簿-编辑/修改已有地址 \n")
        res = init_common_settings.send_request(api_name)
        assert res["success"] is True, "success的值为：%s" % res["success"]
        # assert res['result'][0]['address_id'] is not None, "address_id的值是：%s" % res['result'][0]['address_id']

    # 【我的】地址簿-新增
    @pytest.mark.skip(reason="缺乏测试数据")
    @pytest.mark.parametrize("api_name", ["contact_add"])
    def test_contact_add(self, api_name, init_common_settings):
        print("\n 用例名称：地址簿-新增 \n")
        res = init_common_settings.send_request(api_name)
        assert res["success"] is True, "success的值为：%s" % res["success"]
        # assert res['result'][0]['address_id'] is not None, "address_id的值是：%s" % res['result'][0]['address_id']

    # 【我的】地址簿-删除
    @pytest.mark.skip(reason="缺乏测试数据")
    @pytest.mark.parametrize("api_name", ["contact_remove"])
    def test_contact_remove(self, api_name, init_common_settings):
        print("\n 用例名称：地址簿-删除 \n")
        res = init_common_settings.send_request(api_name)
        assert res["success"] is True, "success的值为：%s" % res["success"]
        # assert res['result'][0]['address_id'] is not None, "address_id的值是：%s" % res['result'][0]['address_id']


if __name__ == "__main__":
    # 运行全部用例
    # pytest.main(['-v', "test_common_settings.py"])
    # 运行地址簿相关用例
    pytest.main(['-v', "test_common_settings.py", "-m=contact"])
