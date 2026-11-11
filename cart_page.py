from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def add_product_to_cart(self):
        self.page.locator(".inventory_item button").first.click()

    def open_cart(self):
        self.page.locator(".shopping_cart_link").click()

    def item_names(self):
        return self.page.locator(".inventory_item_name").all_text_contents()

    def get_cart_item_name(self):
        return self.page.locator(".inventory_item_name").first.text_content()
    