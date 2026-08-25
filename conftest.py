"""pytest 全局配置和 fixtures"""
import json
from pathlib import Path
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def login_page(page):
    """提供 LoginPage 实例"""
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    """提供 InventoryPage 实例"""
    return InventoryPage(page)


@pytest.fixture(scope="session")
def test_users():
    """加载测试用户数据（只加载一次）"""
    root_dir = Path(__file__).parent
    users_file = root_dir / "data" / "users.json"
    with open(users_file, "r", encoding="utf-8") as f:
        return json.load(f)