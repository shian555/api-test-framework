# -*- coding: utf-8 -*-
"""conftest.py —— pytest 的"公共仓库"（v0.3 的核心角色）。

pytest 会自动加载它（不需要 import）：同目录及子目录的所有用例都能用这里的 fixture。

fixture 怎么用（就一条规则）：
    用例函数的参数里写 fixture 的名字，pytest 就会先去执行同名 fixture，
    把返回值塞进这个参数 —— 名字必须一字不差（和字段名一个道理）。

价值：
    client / post_api / user_api 现在全项目只定义一次，谁用谁声明，
    不再复制粘贴；BASE_URL 换环境只改下面这一行。
"""
import pytest

from apis.post_api import PostApi
from apis.user_api import UserApi
from common.api_client import ApiClient

# ★ 全项目唯一的环境地址：换测试环境/生产环境，只改这一行
BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def client():
    """API 客户端：封装好的 Session，所有接口层共用一个"""
    return ApiClient(BASE_URL)


@pytest.fixture
def post_api(client):
    """帖子接口。fixture 也能依赖 fixture：参数里写 client，就能拿到上面准备好的客户端"""
    return PostApi(client)


@pytest.fixture
def user_api(client):
    """用户接口"""
    return UserApi(client)
