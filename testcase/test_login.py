#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
from API.all_api import AllApi
from common.get_log import get_log
logger = get_log()


# 登录模块的测试用例
class TestLogin(object):
    # 登录测试用例初始化，用于处理执行用例前后的数据
    @pytest.fixture(scope="class")
    def init_login(self):
        logger.info("\n ==============================【登录】测试用例开始 ==============================")
        all_login = AllApi()
        return all_login

    # 【登录】分别用邮箱、手机号登录
    # @pytest.mark.skip(reason="邮箱/手机号登录，暂时没必要执行该用例")
    @pytest.mark.parametrize("api_name", ["login_sandbox_email", "login_sandbox_phoneNumber"])
    def test_login_01(self, api_name, init_login):
        print("\n 用例名称：输入正确用户名和密码后，响应内容：\n")
        res = init_login.login(api_name)
        # 断言后面添加提示信息，这样在断言失败时，会自动输出失败原因
        # 断言1：success的值为True
        assert res['success'] is True, "success的值为: %s" % res['success']
        # 断言2：access_token的值为不为空
        assert res['access_token'] is not None, 'access-token的值为：%s' % res['access_token']


if __name__ == "__main__":
    pytest.main(['-s', 'test_login.py'])
    # pytest版本过高，无法识别allure插件，需要降低pytest版本
    # pytest.main(['-v', '-q', '--alluredir', '../report/xml', 'test_login.py'])
    # pytest.main(['-v', 'test_login.py', '--html=report/login_report.html', '--self-contained-html'])
