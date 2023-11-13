"""Conftest file for pytest hooks and fixtures."""

import datetime
from pathlib import Path

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.validate import validate_env_var


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config: pytest.Config) -> None:
    """Handle initial configuration setup."""
    # load environment variables
    load_dotenv()
    validate_env_var("USERNAME")
    validate_env_var("PASSWORD")

    # create reporting directory if not already existing
    reporting_path = Path("reporting")
    if not reporting_path.exists():
        reporting_path.mkdir(parents=True)

    # create a directory with the current date
    reporting_dir = Path(
        f"reporting/{datetime.datetime.now(tz=datetime.UTC).strftime('%d-%m-%Y')}",
    )

    if not reporting_dir.exists():
        reporting_dir.mkdir(parents=True)

    # create a subdirectory for each execution per day
    execution_dir = Path(
        f"{reporting_dir}/{datetime.datetime.now(tz=datetime.UTC).strftime('%d-%m-%Y_%H%M%S')}/",
    )

    # set the command line options for the html and playwright output paths
    if config.getoption("--html") is not None:
        config.option.htmlpath = execution_dir / config.getoption("--html")
    config.option.output = execution_dir / "artifacts"


@pytest.fixture(scope="session", autouse=True)
def base_url() -> str:
    """Fixture to share the base url string."""
    return "https://www.saucedemo.com"


@pytest.fixture()
def login_page(page: Page) -> LoginPage:
    """Initialise a LoginPage instance."""
    return LoginPage(page=page)


@pytest.fixture()
def products_page(page: Page) -> ProductsPage:
    """Initialise a ProductsPage instance."""
    return ProductsPage(page=page)
