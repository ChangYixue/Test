#!/usr/bin/env python
# -*- coding:utf-8 -*-
# fileName: conftest.py
from API.all_api import AllApi
import pytest
from common.get_log import get_log
logger = get_log()

# 在执行所有用例之前先执行登录接口，获取token
@pytest.fixture(scope="session")
def init_token():
    # 正确邮箱/手机号和密码登录
    # logger.info("\n ============================= 在所有用例执行之前，生成token =============================")
    all_login = AllApi()
    logger.info("\n ============================= 在所有用例执行之前，生成token =============================")
    all_login.send_request("login_sandbox_email")
