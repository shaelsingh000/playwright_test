from pages.base_page import BasePage

class InventoryPage(BasePage):
    ADD_TO_CART_BTN = "text=Add to cart"
    CART_ICON = ".shopping_cart_link"

    def add_product_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def go_to_cart(self):
        self.click(self.CART_ICON)