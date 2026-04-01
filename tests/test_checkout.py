from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from data.login_data import valid_user

URL = "https://www.saucedemo.com/"

def test_checkout_flow(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    login.navigate(URL)
    login.login(valid_user["username"], valid_user["password"])

    inventory.add_product_to_cart()
    inventory.go_to_cart()

    cart.checkout()
    checkout.complete_checkout()

    assert "Thank you for your order!" in checkout.get_success_message()