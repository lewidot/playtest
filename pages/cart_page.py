"""Shopping Cart Page class for the Page Object Model."""

from playwright.sync_api import Locator, Page


class CartPage:
    """Page Object Model for the Shopping Cart page."""

    def __init__(self: "CartPage", page: Page) -> None:
        """Construct a CartPage."""
        # Attributes
        self.page: Page = page
        self.url: str = "/cart.html"

        # Locators
        self.cart_item: Locator = self.page.locator(".cart_item")
        self.cart_item_name: Locator = self.page.locator(".inventory_item_name")

    def cart_item_by_name(self: "CartPage", name: str) -> Locator:
        """Filter a cart item Locator by the cart_item_name Locator."""
        return self.cart_item.filter(has=self.cart_item_name.filter(has_text=name))
