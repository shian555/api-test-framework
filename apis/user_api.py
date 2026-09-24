# -*- coding: utf-8 -*-
"""用户接口：一个资源一个类，和 PostApi 平级（这就是"业务接口层"的组织方式）。"""
from common.api_client import ApiClient


class UserApi:
    def __init__(self, client: ApiClient):
        self.client = client

    def get_user(self, user_id):
        """查询用户：GET /users/{id}"""
        return self.client.get(f"/users/{user_id}")
