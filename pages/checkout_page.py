from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    ZIP = "#postal-code"
    CONTINUE = "#continue"
    FINISH = "#finish"
    SUCCESS = ".complete-header"

    def complete_checkout(self):
        self.fill(self.FIRST_NAME, "Test")
        self.fill(self.LAST_NAME, "User")
        self.fill(self.ZIP, "12345")
        self.click(self.CONTINUE)
        self.click(self.FINISH)

    def get_success_message(self):
        return self.get_text(self.SUCCESS)