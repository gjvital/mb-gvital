from playwright.sync_api import Page, expect
import re
from playwright.sync_api import Playwright, sync_playwright, expect
import sys
sys.path.append("C:\\Users\\user_name\\Documents\\MB-project\\development\\") #update to your local pathco
from elements import *
from assertsByGroups import * 


def test_validate_error_message(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_navigation_timeout(300000)
    page.goto(url)

    #test starts
    sleep(5)
    accept_cookies(page)
    fill_location_form(page)
    
    #click the filter button
    page.locator(elements.filter_button).click()
    page.get_by_role("button", name="Pre-Owned").click()

    #site gets redirected when clicked in Pre-Owned tab
    page.goto("https://shop.mercedes-benz.com/en-au/shop/vehicle/srp/used?sort=relevance-ucos&assortment=vehicle")

    #select options inside the filter
    page.locator(elements.filter_button).click()
    page.locator("div").filter(has_text=re.compile(r"^Colour$")).click()
    page.get_by_text("Colour 0").click()
    page.locator(elements.choose_color_dropdown).get_by_text(values.choose_color_dropdown_value).click()

    #sort by price high to low and go to highest price car
    page.get_by_label("Sorting").select_option("price-desc-ucos")
    page.locator("a").filter(has_text="Explore").first.click()

    # Find the element containing the VIN number
    vin_element = page.query_selector('li[data-test-id="dcp-vehicle-details-list-item-11"] .dcp-vehicle-details-list-item__value')

    # Find the element containing the Model Year
    model_year_element = page.query_selector('li[data-test-id="dcp-vehicle-details-list-item-3"] .dcp-vehicle-details-list-item__value')

    # Initialize variables with default values
    vin_number = "VIN number not found."
    model_year = "Model year not found."

    # Check if VIN element is found and extract VIN number
    if vin_element:
        vin_number = vin_element.inner_text()
        print(f"VIN Number: {vin_number}")

    # Check if Model Year element is found and extract Model Year
    if model_year_element:
        model_year = model_year_element.inner_text()
        print(f"Model Year: {model_year}")

    # Write both VIN number and Model Year to a file
    with open('vin_and_model_year.txt', 'w') as file:
        file.write(f"VIN Number: {vin_number}\n")
        file.write(f"Model Year: {model_year}\n")
        print("VIN Number and Model Year written to 'vin_and_model_year.txt' file.")

    #Fill Enquire Now form with Bad data
    page.locator(elements.enquire_now_button).click()
    page.get_by_label(elements.first_name_field).fill(values.first_name_value)
    page.get_by_label(elements.last_name_field).fill(values.last_name_value)
    page.get_by_label(elements.email_field).fill(values.email_value)
    page.locator(elements.contact_field).get_by_label("Phone").fill(values.contact_value)
    page.get_by_label(elements.postal_code_enquire_form).fill(values.postal_code_enquire_form_value)
    page.get_by_label(elements.comment_field).fill(values.comment_value)
    page.locator(elements.enquire_confirmation_send_button).click()

    # Assert the presence of the error message text within a specific element
    
    try:
        error_element = page.locator(elements.error_message_locator).first
        error_text = error_element.text_content()

        expected_text = values.expected_text_value
        assert expected_text in error_text, "Error message not found."
        print("Assertion: Error message found.")
    except AssertionError as e:
        print(f"Assertion failed: {e}")
        raise
    #test ends
    
    context.close()
    browser.close()