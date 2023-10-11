from playwright.sync_api import Page


class ProductsPage:
    """Page Object Model for the Products page."""

    def __init__(self, base_url: str, page: Page) -> None:
        """Construct a ProductsPage."""
        # Attributes
        self.page: Page = page
        self.url: str = f"{base_url}/inventory.html"
        self.title: str = "Swag Labs"

        # Locators

    def load(self) -> None:
        """Load the website url."""
        self.page.goto(url=self.url)
