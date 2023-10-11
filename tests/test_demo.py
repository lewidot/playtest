from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_title(page: Page) -> None:
    """Demo test case."""
    login_page = LoginPage(base_url="https://www.saucedemo.com", page=page)

    # Go to the login page
    login_page.load()

    # Assert the page title
    expect(login_page.page).to_have_title(login_page.title)


def test_login(page: Page) -> None:
    """Test the login page."""

    login_page = LoginPage(base_url="https://www.saucedemo.com", page=page)
    products_page = ProductsPage(base_url="https://www.saucedemo.com", page=page)

    # Go to the login page
    login_page.load()

    # Complete the login page
    login_page.login()

    # Assert that the login is successful
    expect(products_page.page).to_have_url(products_page.url)
