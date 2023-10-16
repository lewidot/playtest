from playwright.sync_api import Page, Locator


class ProductsPage:
    """Page Object Model for the Products page."""

    def __init__(self, base_url: str, page: Page) -> None:
        """Construct a ProductsPage."""
        # Attributes
        self.page: Page = page
        self.url: str = f"{base_url}/inventory.html"
        self.title: str = "Swag Labs"

        # Locators
        self.product: Locator = self.page.locator(".inventory_item")
        self.product_name: Locator = self.page.locator(".inventory_item_name")
        self.product_price: Locator = self.page.locator(".inventory_item_price")
        self.product_description: Locator = self.page.locator(".inventory_item_desc")
        self.product_image: Locator = self.page.locator("img")

    def load(self) -> None:
        """Load the website url."""
        self.page.goto(url=self.url)

    def product_by_name(self, name: str) -> Locator:
        """Filter a product Locator by the product_name Locator."""
        return self.product.filter(has=self.product_name.filter(has_text=name))
