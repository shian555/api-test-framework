"""统一的 HTTP 客户端封装。

为什么要封装（面试必问"你的框架怎么分层的"）：
1. 统一 base_url：换测试环境只改一处配置
2. 统一超时：避免单条请求挂死拖垮整个回归
3. 以后要加登录 token / 日志 / 失败重试，只改这一个文件，所有用例自动生效
"""
import requests


class ApiClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        # Session 会复用 TCP 连接（比每次 requests.get 快），
        # 后面学"接口关联/token 管理"时，就在这里统一加请求头
        self.session = requests.Session()

    def get(self, path: str, **kwargs):
        kwargs.setdefault("timeout", self.timeout)
        return self.session.get(self.base_url + path, **kwargs)

    def post(self, path: str, json=None, **kwargs):
        kwargs.setdefault("timeout", self.timeout)
        return self.session.post(self.base_url + path, json=json, **kwargs)
