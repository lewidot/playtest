from playwright.sync_api import Page, expect


def test_title(page: Page) -> None:
    """Demo test case."""
    page.goto("https://www.saucedemo.com")
    expect(page).to_have_title("Swag Labs")


def test_login(page: Page) -> None:
    """Test the login page."""

    # Go to the login page
    page.goto("https://www.saucedemo.com")

    # Complete the login page
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    # Assert that the login is successful
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
