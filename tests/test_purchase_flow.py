"""商品列表、购物车和结算流程测试。"""
from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestPurchaseFlow:
    def _login(self, login_page, test_users):
        user = test_users["valid_user"]
        login_page.login(user["username"], user["password"])

    def test_sort_products_by_price_low_to_high(self, login_page, inventory_page, test_users):
        """按价格升序排列后，页面商品价格应按升序展示。"""
        self._login(login_page, test_users)
        expect(inventory_page.title).to_have_text("Products")
        inventory_page.sort_products("lohi")
        prices = inventory_page.product_prices()
        assert prices == sorted(prices)

    def test_add_product_to_cart(self, login_page, inventory_page, test_users):
        """加入一个商品后，购物车角标和购物车内容应一致。"""
        self._login(login_page, test_users)
        inventory_page.add_product("Sauce Labs Backpack")
        assert inventory_page.cart_count() == 1
        inventory_page.open_cart()

        cart = CartPage(login_page.page)
        expect(cart.title).to_have_text("Your Cart")
        cart.has_product("Sauce Labs Backpack")

    def test_complete_purchase(self, login_page, inventory_page, test_users):
        """验证从选购商品到订单完成的主流程。"""
        self._login(login_page, test_users)
        inventory_page.add_product("Sauce Labs Backpack")
        inventory_page.open_cart()

        cart = CartPage(login_page.page)
        cart.checkout()
        checkout = CheckoutPage(login_page.page)
        checkout.fill_customer_info("Bo", "Li", "200000")
        checkout.continue_to_overview()
        checkout.finish_order()
