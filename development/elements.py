from environments import *
from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright, sync_playwright, expect

class values():
	# test data
    select_your_location_value = "New South Wales"
    postal_code_value = "2007"
    expected_text_value = 'An error has occurred.Please check the following sections: Please check the data you entered. '
    choose_color_dropdown_value = "BRILLANTBLUE metallic"
    first_name_value = "First Name"
    last_name_value = "Last Name"
    email_value = "E-Mail"
    contact_value = "test"
    postal_code_enquire_form_value = 'Postal'
    comment_value = 'Test'

class elements():

    # cookies
    cookies_confirmation_button = "[data-test-id=\"handle-accept-all-button\"]"
    
    #Portal Code
    postal_code_field = "[data-test-id=\"modal-popup__location\"]"
    continue_button_select_location = "[data-test-id=\"state-selected-modal__close\"]"
    filter_button = "#app > div.dcp-shop > main > div.dcp-shop__container > div.dcp-cars-srp > div.wrapper > div.sidebar > span"  # need to check for a better locator with dev team, this works at the moment.
    error_message_locator = '.dcp-error-message'
    choose_color_dropdown = "[data-test-id=\"multi-select-dropdown\"]"
    enquire_now_button = "[data-test-id=\"dcp-buy-box__contact-seller\"]"
    first_name_field = "First Name"
    last_name_field = "Last Name"
    email_field = "E-Mail"
    contact_field = "[data-test-id=\"rfq-contact__phone\"]"
    postal_code_enquire_form = "Postal Code"
    comment_field = "Comments (optional)"
    enquire_confirmation_send_button = "[data-test-id=\"dcp-rfq-contact-button-container__button-next\"]"
    