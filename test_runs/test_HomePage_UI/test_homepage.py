from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
from playwright.sync_api import Page
from DOMs.HomePage import HomePage


def test_run_homePage(page: Page) -> None:

    page.goto("https://www.reno-reno.pl/")




    # ---------------------




