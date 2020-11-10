#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author lubosson
# @since 2020-08-06
# @description --
import threading


def auth_token() -> str:
    return "token"


class WeChatAuthTask(threading.Thread):
    def __init__(self, func):
        super(WeChatAuthTask, self).__init__()
        self.func = func
        self.result = self.func

    def get(self):
        threading.Thread.join(self)
        try:
            return self.result
        except Exception:
            return None

    def run(self) -> str:
        return "token"

