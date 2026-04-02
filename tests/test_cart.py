import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from data.login_data import valid_user
from utils.logger import get_logger
from utils.config import CONFIG,ENV

URL = CONFIG[ENV]["base_url"]
logger = get_logger(__name__)

logger.info("Starting Add to Cart test")

@pytest.mark.smoke
@pytest.mark.cart
def test_add_to_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    logger.info("Navigating to Login page")
    login.navigate(URL)
    logger.info("Logging into the site")
    login.login(valid_user["username"], valid_user["password"])
    logger.info("Add product to the cart")
    inventory.add_product_to_cart()
    logger.info("Going to the cart page")
    inventory.go_to_cart()
    logger.info("Asserting that out poduct is present in the cart")
    assert cart.get_product_name() is not None