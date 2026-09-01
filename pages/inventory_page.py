"""登录成功后的商品列表页面。"""
import re

from playwright.sync_api import Page
from playwright.sync_api import expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.shopping_cart = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.product_sort = page.locator("[data-test='product-sort-container']")
        self.products = page.locator(".inventory_item")

    def is_loaded(self):
        """验证页面是否加载成功"""
        return self.title.is_visible() and self.title.text_content() == "Products"

    def sort_products(self, option: str):
        self.product_sort.select_option(option)

    def product_prices(self):
        prices = self.products.locator(".inventory_item_price").all_text_contents()
        return [float(re.sub(r"[^0-9.]", "", price)) for price in prices]

    def add_product(self, product_name: str):
        product = self.products.filter(has_text=product_name)
        expect(product).to_have_count(1)
        product.get_by_role("button", name=re.compile("Add to cart", re.I)).click()

    def cart_count(self):
        return int(self.cart_badge.inner_text()) if self.cart_badge.is_visible() else 0

    def open_cart(self):
        self.shopping_cart.click()
