from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BTN = "#checkout"
    ITEM_NAME = ".inventory_item_name"

    def get_product_name(self):
        return self.get_text(self.ITEM_NAME)

    def checkout(self):
        self.click(self.CHECKOUT_BTN)