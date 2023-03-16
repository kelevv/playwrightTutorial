import time
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage

@pytest.mark.smoke
def test_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    homepage = HomePage(page)
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    page.click("'Log In'", timeout=2000)
    page.click("'Log In'", timeout=2000)
    time.sleep(1)
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_test_id("siteMembersDialogLayout").get_by_test_id("buttonElement").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.storozhenko@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("test123")
    page.get_by_label("Password").press("Enter")
    page.wait_for_load_state("networkidle")
    time.sleep(3)
    expect(homepage.celebrate_header).to_be_visible()
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()
    # ---------------------
    context.close()
    browser.close()
