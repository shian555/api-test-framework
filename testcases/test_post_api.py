# -*- coding: utf-8 -*-
"""第一组真实接口用例：查询帖子 + 创建帖子。

断言分三层（面试题"断言怎么设计"的标准答案雏形）：
1. 状态码 —— 服务通不通
2. 响应结构 —— 字段在不在、类型对不对
3. 业务值 —— 数据对不对

v0.3 变化：开头的 BASE_URL/client/post_api 三行搬进了 conftest.py 的 fixture——
用例在参数里声明同名变量就能拿到现成的，文件开头干干净净。
"""


def test_get_post_success(post_api):
    """正常场景：查询存在的帖子 id=1"""
    resp = post_api.get_post(1)
    # 第 1 层：状态码
    assert resp.status_code == 200
    data = resp.json()
    # 第 2 层：响应结构
    assert "userId" in data
    assert "title" in data
    assert "body" in data
    # 第 3 层：业务值
    assert data["id"] == 1
    assert data["title"] != ""


def test_get_post_not_exist(post_api):
    """异常场景：查询不存在的帖子，应返回 404 而不是 500

    注意：这行也要声明 post_api 参数——fixture 是"谁用谁声明"，
    不声明它就不存在（和上一版的模块级变量不同）。
    """
    resp = post_api.get_post(99999)
    assert resp.status_code == 404


def test_create_post_success(post_api):
    """正常场景：创建帖子，返回 201 且参数回显正确（第一个手写用例 2026-09-23）"""
    resp = post_api.create_post(title="赵敏的测试帖子", body="这是内容", user_id=1)
    # 第 1 层：状态码（创建成功 = 201 Created，不是 200）
    assert resp.status_code == 201
    data = resp.json()
    # 第 2 层：响应结构
    assert "id" in data
    assert "title" in data
    # 第 3 层：业务值（接口应把传参原样回显）
    assert data["title"] == "赵敏的测试帖子"
    assert data["body"] == "这是内容"
    assert data["userId"] == 1
