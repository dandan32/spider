#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author: dandan<pipidingdingting@163.com>
# Created on 2018/11/8 23:55
# file: Fetcher.py
from abc import ABCMeta, abstractmethod
from http import HTTPStatus


print(HTTPStatus.OK)


class Fetcher:
    """抓取器"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def fetch(self, request):
        pass


class AsyncFetcher(Fetcher):
    """异步抓取"""
    pass


class SyncFetcher(Fetcher):
    """同步抓取"""
    pass
