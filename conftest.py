"""pytest 全局配置和 fixtures"""
import json
import logging
from pathlib import Path
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


logger = logging.getLogger(__name__)


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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """测试失败时额外保存截图，方便在本地和 CI 定位问题。"""
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return

    page = item.funcargs.get("page")
    if page is None or page.is_closed():
        return

    output_dir = Path(item.config.getoption("--output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    screenshot = output_dir / f"{item.name}.png"
    try:
        page.screenshot(path=str(screenshot), full_page=True)
        logger.info("失败截图已保存：%s", screenshot)
        try:
            import allure
            allure.attach.file(str(screenshot), name=f"{item.name} screenshot", attachment_type=allure.attachment_type.PNG)
        except ImportError:
            pass
    except Exception as exc:
        logger.warning("保存失败截图失败：%s", exc)
