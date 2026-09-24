# api-test-framework 接口自动化测试框架（建设中）

基于 `pytest + requests` 的接口自动化框架，从 0 开始逐层搭建。

## 分层结构

```
api-test-framework/
├── common/api_client.py    # HTTP 客户端封装（Session 复用、统一超时）
├── apis/                   # 业务接口层：一个资源一个类（PostApi / UserApi）
├── testcases/              # 测试用例层：只写业务，断言分三层（状态码/结构/业务值）
├── conftest.py             # fixture：client / post_api / user_api，BASE_URL 全项目唯一
├── pytest.ini              # pytest 配置
└── requirements.txt
```

## 运行

```bash
pip install -r requirements.txt
python -m pytest -v   # 4 passed
```

## 当前能力（随学习更新）

- [x] v0.1：GET 接口正常/异常场景，三层断言（状态码/结构/业务值）
- [x] v0.2：POST 创建接口 + 第一个手写用例
- [x] v0.3：fixture 前置管理——环境地址全项目唯一，谁用谁声明
- [ ] 参数化（数据驱动）
- [ ] 接口关联（如登录 token 传递）
- [ ] Allure 报告 + CI 接入
