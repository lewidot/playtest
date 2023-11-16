"""Products Page class for the Page Object Model."""

from playwright.sync_api import Locator, Page


class ProductsPage:
    """Page Object Model for the Products page."""

    def __init__(self: "ProductsPage", page: Page) -> None:
        """Construct a ProductsPage."""
        # Attributes
        self.page: Page = page
        self.url: str = "/inventory.html"
        self.title: str = "Swag Labs"

        # Locators
        self.product: Locator = self.page.locator(".inventory_item")
        self.product_name: Locator = self.page.locator(".inventory_item_name")
        self.product_price: Locator = self.page.locator(".inventory_item_price")
        self.product_description: Locator = self.page.locator(".inventory_item_desc")
        self.product_image: Locator = self.page.locator("img")
        self.product_add_to_cart: Locator = self.page.get_by_text("Add to cart")
        self.shopping_cart_link: Locator = self.page.locator(".shopping_cart_link")

    def load(self: "ProductsPage") -> None:
        """Load the website url."""
        self.page.goto(url=self.url)

    def click_shopping_cart(self: "ProductsPage") -> None:
        """Click the shopping cart link."""
        self.shopping_cart_link.click()

    def product_by_name(self: "ProductsPage", name: str) -> Locator:
        """Filter a product Locator by the product_name Locator."""
        return self.product.filter(has=self.product_name.filter(has_text=name))

    def add_product_to_cart(self: "ProductsPage", name: str) -> None:
        """Locate a product and add it to the cart."""
        product = self.product_by_name(name)
        product.locator(self.product_add_to_cart).click()
