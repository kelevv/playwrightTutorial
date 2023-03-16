import pytest
from playwright.sync_api import Playwright, sync_playwright
from pom.contact_us_page import ContactUsPage


@pytest.mark.integration
def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form("Symon", "123 Main", "test@email.com", "123-432-5435", "test subject", "test message")
