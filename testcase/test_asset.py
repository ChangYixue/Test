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


if __name__ == "__main__":
    # 若存在多个标记，则用or连接，形成一个测试集，比如'-m=assetList or test or allLists'
    pytest.main(['-s', 'test_asset.py', '-m=test'])
    # pytest.main(['-v', 'test_asset.py', '--html=report/asset_report.html', '--self-contained-html'])


