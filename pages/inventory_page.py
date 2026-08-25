"""登录成功后的商品列表页面"""
from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.shopping_cart = page.locator(".shopping_cart_link")

    def is_loaded(self):
        """验证页面是否加载成功"""
        return self.title.is_visible() and self.title.text_content() == "Products"