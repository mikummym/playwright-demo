# playwright-demo

基于 Python + Playwright + pytest 的 Web UI 自动化测试框架 Demo，使用 SauceDemo 公开测试网站演示 Page Object Model、数据驱动、业务流测试和失败诊断。

## 覆盖范围

- 登录：正常登录、密码错误、空密码、锁定用户
- 商品列表：按价格升序排序并校验结果
- 购物车：加入商品后角标数量与购物车内容一致
- 结算：从选购商品到提交订单的完整主流程

## 项目结构

```text
playwright-demo/
├── pages/                 # Page Object Model
│   ├── base_page.py       # 页面基类：输入、点击、等待、重试
│   ├── login_page.py      # 登录页
│   ├── inventory_page.py  # 商品列表页：排序、加购、购物车入口
│   ├── cart_page.py       # 购物车页
│   └── checkout_page.py   # 结算页：填写信息、确认、完成订单
├── tests/
│   ├── test_login.py          # 登录场景
│   └── test_purchase_flow.py  # 排序、加购、结算主流程
├── data/users.json        # 测试数据（数据驱动）
├── conftest.py            # fixture、失败截图钩子
├── pytest.ini             # pytest 与失败诊断配置
└── .github/workflows/     # GitHub Actions CI
```

## 本地运行

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
pytest
```

## 失败诊断

测试失败时自动保留以下产物，便于快速定位问题：

- 失败页面全屏截图（`test-results/` 下，并附加到 Allure 报告）
- Playwright trace（`test-results/` 下，可在 [trace.playwright.dev](https://trace.playwright.dev) 回放）
- 失败用例视频

生成 JUnit 与 Allure 原始数据：

```powershell
pytest --junitxml=test-results/junit.xml --alluredir=test-results/allure-results
```

## CI

GitHub Actions 会在 push / pull request 时安装依赖与 Chromium、执行测试，并上传 JUnit、Allure 原始数据、截图、trace 与视频产物，便于在 CI 中直接排查失败。

## 设计模式

- **Page Object Model (POM)**：每个页面封装为一个类，元素操作与业务断言解耦
- **Fixture 管理**：通过 conftest.py 管理页面对象、测试数据与失败钩子
- **数据驱动**：测试数据独立存放于 JSON，便于维护与扩展

## 技术栈

Python 3.10+、Playwright、pytest、pytest-playwright、Allure Pytest、GitHub Actions
