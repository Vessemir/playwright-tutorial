import pytest
from playwright.sync_api import Page

class HomePage():
    URL = 'https://www.reno-reno.pl/'
    def __init__(self, page: Page) -> None:
        self.page = page
    def goTo(self):
        self.page.goto("https://www.reno-reno.pl/")