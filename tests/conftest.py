from datetime import datetime
import os
import pytest
from pytest import Config
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config: Config) -> None:
    # create reporting directory if not already existing
    if not os.path.exists("reporting"):
        os.makedirs("reporting")

    # create a directory with the current date
    reporting_dir = f"reporting/{datetime.now().strftime('%d-%m-%Y')}"

    if not os.path.exists(reporting_dir):
        os.makedirs(reporting_dir)

    # create a subdirectory for each execution per day
    execution_dir = f"{reporting_dir}/{datetime.now().strftime('%d-%m-%Y_%H%M%S')}/"

    # set the command line options for the html and playwright output paths
    if config.getoption("--html") is not None:
        config.option.htmlpath = execution_dir + config.getoption("--html")
    config.option.output = execution_dir + "artifacts"


@pytest.fixture(scope="session", autouse=True)
def base_url() -> str:
    """Fixture to share the base url string."""
    return "https://www.saucedemo.com"


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Initialise a LoginPage instance"""
    return LoginPage(page=page)


@pytest.fixture
def products_page(page: Page) -> ProductsPage:
    """Initialise a ProductsPage instance"""
    return ProductsPage(page=page)
