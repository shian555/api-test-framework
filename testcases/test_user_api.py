# -*- coding: utf-8 -*-
"""第二个用例文件（v0.3 版）。

对比上一版：开头的 BASE_URL/client/user_api 三行重复消失了——
用例只要在参数里声明 user_api，conftest.py 就会送过来。
这就是 fixture 解决的问题：准备工作全项目写一次，处处声明使用。
"""


def test_get_user_success(user_api):
    """正常场景：查询存在的用户 id=1"""
    resp = user_api.get_user(1)
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == 1
