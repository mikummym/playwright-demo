# playwright-demo
    
基于 Python + Playwright + pytest 的 Web UI 自动化测试框架 Demo。

## 测试目标

使用 [SauceDemo](https://www.saucedemo.com) 作为公开测试网站，验证登录功
能。

## 项目结构
    
playwright-demo/    
├── conftest.py          # pytest fixtures  
├── pages/               # Page Object Model    
  ├── base_page.py     # 页面基类   
  ├── login_page.py    # 登录页    
  └── inventory_page.py # 商品列表页     
├── tests/               # 测试用例     
  └── test_login.py    # 登录测试       
└── data/                # 测试数据     
└── users.json
    
## 环境搭建
    
1. 创建虚拟环境   
────────────────────────────────────────    
python -m venv venv

2. 激活虚拟环境（Windows）    
────────────────────────────────────────     
venv\Scripts\activate

3. 安装依赖  
────────────────────────────────────────     
pip install -r requirements.txt

4. 安装 Playwright 浏览器     
────────────────────────────────────────     
playwright install chromium
    
## 运行测试
    
pytest -v
    
## 设计模式
    
- **Page Object Model (POM)**：每个页面封装为一个类，操作和断言解耦
- **Fixture 管理**：通过 conftest.py 管理页面对象和测试数据
- **数据驱动**：测试数据存储在 JSON 文件中，便于维护

## 技术栈

- Python 3.10+
- Playwright
- pytest
- Page Object Model
