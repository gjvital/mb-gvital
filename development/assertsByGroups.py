from environments import *
from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect
from elements import *
from time import sleep

# reuse of repetitive functions
def accept_cookies(page):
    page.get_by_role("button", name="Agree to all").click()

def fill_location_form(page):
    page.get_by_label("* Your state").select_option(values.select_your_location_value)
    page.locator(elements.postal_code_field).get_by_label("", exact=True).fill(values.postal_code_value)
    page.locator("label").filter(has_text="Private").locator("div").click()
    page.locator(elements.continue_button_select_location).click()