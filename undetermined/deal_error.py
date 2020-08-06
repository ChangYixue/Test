#!/usr/bin/env python
# -*- coding:utf-8 -*-


class AssetException(Exception):
    ERROR_INTERNAL_ERROR = 1000000


def show_me():
    try:
        raise AssetException(AssetException.ERROR_INTERNAL_ERROR, "aaaaaaaaa")
    except Exception as e:
        print(e)