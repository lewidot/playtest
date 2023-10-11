import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Initialise a LoginPage instance"""
    return LoginPage(base_url="https://www.saucedemo.com", page=page)


@pytest.fixture
def products_page(page: Page) -> ProductsPage:
    """Initialise a ProductsPage instance"""
    return ProductsPage(base_url="https://www.saucedemo.com", page=page)
