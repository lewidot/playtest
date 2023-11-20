"""File containing common interactions grouped into Flows."""


from dataclasses import dataclass

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@dataclass
class Flows:
    """Class for methods that group interactions across pages."""

    login_page: LoginPage
    products_page: ProductsPage

    def add_product_to_cart(
        self: "Flows",
        product_name: str = "Sauce Labs Backpack",
    ) -> None:
        """Login, add a product to the cart and navigate to the cart page."""
        # Login to the website
        self.login_page.load()
        self.login_page.login()

        # Locate and add an item to the cart
        self.products_page.add_product_to_cart(name=product_name)

        # Navigate to the cart page
        self.products_page.click_shopping_cart()
