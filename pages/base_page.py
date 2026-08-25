"""页面基类，封装通用操作"""
from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def fill(self, locator: Locator, content: str):
        """输入文本"""
        locator.fill(content)

    def click(self, locator: Locator):
        """点击元素"""
        locator.click()

    def get_text(self, locator: Locator):
        """获取文本内容"""
        return locator.text_content()

    def wait_for_visible(self, locator: Locator, timeout: float = 5000):
        """等待元素可见"""
        locator.wait_for(state="visible", timeout=timeout)

    def goto(self, url: str):
        """页面跳转"""
        self.page.goto(url)

    def safe_click(self, locator: Locator, retries: int = 2):
        """带重试的点击，处理偶发加载延迟"""
        for i in range(retries + 1):
            try:
                locator.click()
                return
            except Exception:
                if i == retries:
                    raise
                self.page.wait_for_timeout(500)