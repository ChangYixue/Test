#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 序列号方法、获取私钥和签名（expected_signature）
'''
签名验签的大方向无非就是：客户端与服务端约定好，按照统一算法，统一参数，统一顺序，统一密钥 进行加密，然后作对比；我这里就介绍一种比较简单实用且常用的签名/验签方式思路：
客户端：
    签名通过header传到服务端，key名为：token
      签名：API版本号+AK+签名过期时间+密钥(SK)+URL+requestMethod+客户端已排序的参数 做加密；
        加密算法：MD5；
        密钥（SK）: 前后端统一,签名加密的时候使用相当于加盐；
        AK : 多客户端使用不同的SK, 服务端就需要通过AK找到对应的SK进行加密验签；
        签名过期时间：客户端定义的签名过期时间，超过该时间该签名请求不可通过；
    请求参数：已排序的参数通过request-line 或 request-body传到服务端
服务端：
     同样的方式进行签名，验证。以确认调用者是否合法，这就是接口签名验证的思路
'''
import urlencode
import hashlib
import force_bytes
import hmac


def test():
    # 空字典
    params = {}
    # 把参数字典的键值对更新到params里，参数是啥？
    params.update({}) # data
    params.update({}) # data
    # 循环输出键值对？值都是什么？
    params = [(key, val[0]) for key, val in params.items()]
    # 排序？
    params.sort(key=lambda x: x[0])
    # 参数序列号
    blob = "%s|%s|%s|%s" % (
        method, # 接口请求方法？
        path, # 啥路径？
        nonce,  # nonce是时间戳
        urlencode(params, quote_via=quote, safe="-_.!~*'()"), # quote是啥？
    )

    # 获取私钥
    private_key = hashlib.sha256(
        hashlib.sha256(force_bytes(version)).digest() # version是app的版本？
    ).digest()

    # 哈希容器，获取签名结果
    h = hmac.new(force_bytes(private_key), digestmod=hashlib.sha256)
    h.update(force_bytes(blob))

    # 把HTTP_APP_SIG放在headers里，并且expected_signature前面要加上1

    expected_signature = force_bytes(h.digest())  # HTTP_APP_SIG：1expected_signature
