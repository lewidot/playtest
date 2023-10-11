import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.fixture(scope="session")
def base_url() -> str:
    """Fixture to share the base url string."""
    return "https://www.saucedemo.com"


@pytest.fixture
def login_page(page: Page, base_url: str) -> LoginPage:
    """Initialise a LoginPage instance"""
    return LoginPage(base_url=base_url, page=page)


@pytest.fixture
def products_page(page: Page, base_url: str) -> ProductsPage:
    """Initialise a ProductsPage instance"""
    return ProductsPage(base_url=base_url, page=page)
