from playwright.sync_api import Page, Locator


class LoginPage:
    """Page Object Model for the Login page."""

    def __init__(self, page: Page) -> None:
        """Construct a LoginPage."""
        # Attributes
        self.page: Page = page
        self.url: str = "/"
        self.title: str = "Swag Labs"

        # Locators
        self.username_input: Locator = self.page.get_by_placeholder("Username")
        self.password_input: Locator = self.page.get_by_placeholder("Password")
        self.login_btn: Locator = self.page.get_by_role("button", name="Login")

    def load(self) -> None:
        """Load the website url."""
        self.page.goto(url=self.url)

    def login(self) -> None:
        """Complete the login form."""
        self.username_input.fill("standard_user")
        self.password_input.fill("secret_sauce")
        self.login_btn.click()
