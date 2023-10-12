from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


import pytest


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


@pytest.mark.parametrize(
    "product_name",
    (
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)",
    ),
)
def test_product_is_visible(
    login_page: LoginPage, products_page: ProductsPage, product_name: str
) -> None:
    """Test the expected product is visible on the products page."""

    # Go to the login page
    login_page.load()

    # Complete the login page
    login_page.login()

    # Assert that the product is visible
    expect(products_page.product_name.filter(has_text=product_name)).to_be_visible()
