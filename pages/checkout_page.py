"""Checkout Page class for the Page Object Model."""

from playwright.sync_api import Locator, Page


class CheckoutPage:
    """Page Object Model for the Checkout page."""

    def __init__(self: "CheckoutPage", page: Page) -> None:
        """Construct a CheckoutPage."""
        # Attributes
        self.page: Page = page
        self.url: str = "/checkout-step-one.html"

        # Locators
        self.first_name_input: Locator = self.page.get_by_placeholder("First Name")
        self.last_name_input: Locator = self.page.get_by_placeholder("Last Name")
        self.zip_postal_code_input: Locator = self.page.get_by_placeholder(
            "Zip/Postal Code",
        )
        self.continue_btn: Locator = self.page.get_by_text("Continue")
        self.first_name_error: Locator = self.page.get_by_text(
            "Error: First Name is required",
        )
        self.last_name_error: Locator = self.page.get_by_text(
            "Error: Last Name is required",
        )

    def input_first_name(self: "CheckoutPage", name: str) -> None:
        """Input text into the first name input field."""
        self.first_name_input.fill(name)

    def input_last_name(self: "CheckoutPage", name: str) -> None:
        """Input text into the last name input field."""
        self.last_name_input.fill(name)

    def input_postal_code(self: "CheckoutPage", postcode: str) -> None:
        """Input text into the zip/postal code input field."""
        self.zip_postal_code_input.fill(postcode)

    def click_continue_button(self: "CheckoutPage") -> None:
        """Click the continue button."""
        self.continue_btn.click()
