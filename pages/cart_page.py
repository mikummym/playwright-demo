"""购物车页面对象。"""
from playwright.sync_api import Page
from playwright.sync_api import expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.items = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")

    def is_loaded(self):
        return self.title.is_visible() and self.title.text_content() == "Your Cart"

    def has_product(self, product_name: str):
        product = self.items.filter(has_text=product_name)
        expect(product).to_have_count(1)

    def checkout(self):
        self.checkout_button.click()
