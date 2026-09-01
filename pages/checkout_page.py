"""结算流程页面对象。"""
from playwright.sync_api import Page
from playwright.sync_api import expect


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.complete_header = page.locator(".complete-header")

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_to_overview(self):
        self.continue_button.click()
        expect(self.title).to_contain_text("Overview")

    def finish_order(self):
        self.finish_button.click()
        expect(self.complete_header).to_have_text("Thank you for your order!")
