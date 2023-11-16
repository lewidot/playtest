"""Collection of test cases demonstrating various techniques."""

import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.load_data import load_data


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
    "name",
    [
        ("Sauce Labs Backpack"),
        ("Sauce Labs Bike Light"),
        ("Sauce Labs Bolt T-Shirt"),
        ("Sauce Labs Fleece Jacket"),
        ("Sauce Labs Onesie"),
        ("Test.allTheThings() T-Shirt (Red)"),
    ],
)
def test_product_is_visible(
    login_page: LoginPage,
    products_page: ProductsPage,
    name: str,
) -> None:
    """Test the expected product is visible on the products page."""
    # Go to the login page
    login_page.load()

    # Complete the login page
    login_page.login()

    # Assert that the product is visible
    expect(products_page.product_by_name(name=name)).to_be_visible()


@pytest.mark.parametrize(
    ("name", "price"),
    load_data("./data/product_prices.csv"),
)
def test_product_price(
    login_page: LoginPage,
    products_page: ProductsPage,
    name: str,
    price: str,
) -> None:
    """Test the price is correct for each product on the products page."""
    # Go to the login page
    login_page.load()

    # Complete the login page
    login_page.login()

    # Locate the product by the product name
    product = products_page.product_by_name(name=name)

    # Assert that the product price is correct
    expect(product.locator(products_page.product_price)).to_contain_text(price)


@pytest.mark.parametrize(
    ("name", "description"),
    load_data("./data/product_descriptions.json"),
)
def test_product_description(
    login_page: LoginPage,
    products_page: ProductsPage,
    name: str,
    description: str,
) -> None:
    """Test the description text is correct for each product on the products page."""
    # Go to the login page
    login_page.load()

    # Complete the login page
    login_page.login()

    # Locate the product by the product name
    product = products_page.product_by_name(name=name)

    # Assert that the product description is correct
    expect(product.locator(products_page.product_description)).to_have_text(description)


@pytest.mark.parametrize(("name", "src"), load_data("./data/product_images.xlsx"))
def test_product_img_src(
    login_page: LoginPage,
    products_page: ProductsPage,
    name: str,
    src: str,
) -> None:
    """Test the product image src is correct for each product on the products page."""
    # Go to the login page
    login_page.load()

    # Complete the login page
    login_page.login()

    # Locate the product by the product name
    product = products_page.product_by_name(name=name)

    # Assert that the product description is correct
    expect(product.locator(products_page.product_image)).to_have_attribute(
        name="src",
        value=src,
    )
