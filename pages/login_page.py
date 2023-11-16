"""Login Page class for the Page Object Model."""

import os

from playwright.sync_api import Locator, Page


class LoginPage:
    """Page Object Model for the Login page."""

    def __init__(self: "LoginPage", page: Page) -> None:
        """Construct a LoginPage."""
        # Attributes
        self.page: Page = page
        self.url: str = "/"
        self.title: str = "Swag Labs"
        self.username: str = os.environ["USERNAME"]
        self.password: str = os.environ["PASSWORD"]

        # Locators
        self.username_input: Locator = self.page.get_by_placeholder("Username")
        self.password_input: Locator = self.page.get_by_placeholder("Password")
        self.login_btn: Locator = self.page.get_by_role("button", name="Login")

    def load(self: "LoginPage") -> None:
        """Load the website url."""
        self.page.goto(url=self.url)

    def login(self: "LoginPage") -> None:
        """Complete the login form."""
        self.username_input.fill(self.username)
        self.password_input.fill(self.password)
        self.login_btn.click()
