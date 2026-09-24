"""业务接口层：一个接口一个方法。

为什么单独一层（面试必问）：
接口路径、参数变了只改这里；测试用例里只写业务含义，不写 URL 和参数拼接。
这就叫"分层"——改哪儿都知道去哪儿改。
"""
from common.api_client import ApiClient


class PostApi:
    def __init__(self, client: ApiClient):
        self.client = client

    def get_post(self, post_id: int):
        """查询单篇帖子"""
        return self.client.get(f"/posts/{post_id}")

    def create_post(self, title: str, body: str, user_id: int):
        """创建帖子（jsonplaceholder 是练习环境：返回 201 但不真存数据）"""
        payload = {"title": title, "body": body, "userId": user_id}
        return self.client.post("/posts", json=payload)
