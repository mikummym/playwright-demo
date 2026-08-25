"""登录功能测试用例"""
import pytest
from playwright.sync_api import expect


class TestLogin:

    def test_valid_login(self, login_page, test_users):
        """正常登录：验证登录后跳转到商品列表页"""
        user = test_users["valid_user"]
        login_page.login(user["username"], user["password"])
        expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def test_invalid_password(self, login_page, test_users):
        """密码错误：验证显示错误提示"""
        user = test_users["invalid_user"]
        login_page.login(user["username"], user["password"])
        error = login_page.get_error_message()
        assert "Username and password do not match" in error

    def test_empty_password(self, login_page, test_users):
        """空密码：验证显示必填提示"""
        user = test_users["valid_user"]
        login_page.login(user["username"], "")
        error = login_page.get_error_message()
        assert "Password is required" in error

    def test_locked_out_user(self, login_page, test_users):
        """锁定用户：验证锁定提示"""
        user = test_users["locked_out_user"]
        login_page.login(user["username"], user["password"])
        error = login_page.get_error_message()
        assert "locked out" in error.lower()