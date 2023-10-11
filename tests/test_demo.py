from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_title(login_page: LoginPage) -> None:
    """Demo test case."""

    # Go to the login page
    login_page.load()

    # Assert the page title
    expect(login_page.page).to_have_title(login_page.title)


def test_login(login_page: LoginPage, products_page: ProductsPage) -> None:
    """Test the login page."""

    # Go to the login page
    login_page.load()

    # Complete the login page
    login_page.login()

    # Assert that the login is successful
    expect(products_page.page).to_have_url(products_page.url)
