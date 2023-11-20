"""Conftest file for pytest hooks and fixtures."""

from pathlib import Path
from typing import Any, Generator

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

from flows.flows import Flows
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config: pytest.Config) -> None:
    """Handle initial configuration setup."""
    # load environment variables
    load_dotenv()

    # create reporting directory if not already existing
    report_path = Path("reports")
    if not report_path.exists():
        report_path.mkdir(parents=True)

    # set the command line options for the html report path
    if config.getoption("--html") is not None:
        report_name = str(config.getoption("--html"))
        config.option.htmlpath = report_path / report_name

    # set the command line options for the pytest-playwright output
    config.option.output = report_path / "artifacts"


@pytest.fixture(scope="session", autouse=True)
def base_url() -> str:
    """Fixture to share the base url string."""
    return "https://www.saucedemo.com"


@pytest.fixture()
def _reset_app_state(
    login_page: LoginPage,
    base_page: BasePage,
) -> Generator[None, Any, None]:
    """Reset the app state after each test."""
    yield
    login_page.load()
    login_page.login()
    base_page.reset_app_state()


@pytest.fixture()
def base_page(page: Page) -> BasePage:
    """Initialise a BasePage instance."""
    return BasePage(page=page)


@pytest.fixture()
def login_page(page: Page) -> LoginPage:
    """Initialise a LoginPage instance."""
    return LoginPage(page=page)


@pytest.fixture()
def products_page(page: Page) -> ProductsPage:
    """Initialise a ProductsPage instance."""
    return ProductsPage(page=page)


@pytest.fixture()
def cart_page(page: Page) -> CartPage:
    """Initialise a CartPage instance."""
    return CartPage(page=page)


@pytest.fixture()
def checkout_page(page: Page) -> CheckoutPage:
    """Initialise a CheckoutPage instance."""
    return CheckoutPage(page=page)


@pytest.fixture()
def flows(login_page: LoginPage, products_page: ProductsPage) -> Flows:
    """Initialise a Flows instance."""
    return Flows(login_page, products_page)
