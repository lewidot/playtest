"""Base Page class for the Page Object Model."""

from playwright.sync_api import Locator, Page


class BasePage:
    """Page Object Model for shared locators and interactions."""

    def __init__(self: "BasePage", page: Page) -> None:
        """Construct a BasePage."""
        # Attributes
        self.page: Page = page

        # Locators
        self.burger_menu_icon: Locator = self.page.locator("#react-burger-menu-btn")
        self.reset_app_state_btn: Locator = self.page.get_by_text("Reset App State")

    def click_burger_menu(self: "BasePage") -> None:
        """Click the burger menu icon."""
        self.burger_menu_icon.click()

    def reset_app_state(self: "BasePage") -> None:
        """Open the menu and click the 'Reset App State' button."""
        self.click_burger_menu()
        self.reset_app_state_btn.click()
