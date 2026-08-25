"""登录页面对象"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com"

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("h3[data-test='error']")

    def goto(self):
        self.page.goto(self.URL)

    def fill_username(self, username: str):
        self.username_input.fill(username)

    def fill_password(self, password: str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username: str, password: str):
        """执行登录操作"""
        self.goto()
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()

    def get_error_message(self):
        """获取错误提示文本"""
        return self.error_message.text_content()