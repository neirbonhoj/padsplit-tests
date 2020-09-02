import os
import time
from behave import *

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

PATH = os.getcwd() + "/steps/chromedriver"
driver = webdriver.Chrome(PATH)

current_milli_time = lambda: int(round(time.time() * 1000))

###
# Visiting the PadSplit Staging Website
###

# Tells Google Chrome to visit PadSplit's website
@given('we are on the PadSplit staging website')
def step_impl(context):
	driver.get("https://staging.padsplit.com")
	pass

# Verifies that the website has loaded and is on the home page
@then('the site title should read "Home | PadSplit"')
def step_impl(context):
	assert driver.title == "Home | PadSplit", "Not on the PadSplit home page"


###
# Opening the PadSplit sign up form
###

# Presses the "Get Started" button on PadSplit's navigation bar
@when('we click the get started button')
def step_impl(context):
	get_started_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id="app-bar__create-account-btn"]'))
    )
	get_started_button.click();
	pass

# Verifies that the sign up dialog container has opened
@then('the sign up dialog should appear')
def step_impl(context):
	try:
		sign_up_window = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id="sign-up-dlg"]'))
	    )
		assert sign_up_window.is_displayed()
	except NoSuchElementException:
		assert False, "No sign up dialog"
	

###
# Creating a PadSplit account
###

# Step used for readability in the .feature file - not fundamentally necessary (yet)
@given('the sign up form is open')
def step_impl(context):
	pass

# Inputs test data for the sign up form
@when('we fill out the member sign up form')
def step_impl(context):
	email_input_field = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id="sign-up-dlg__email-fld"]'))
	)
	email_input_field.send_keys('test.email'+str(current_milli_time())+'@gmail.com')

	first_name_input_field = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id="sign-up-dlg__first-name-fld"]'))
	)
	first_name_input_field.send_keys('TestFirstName')

	last_name_input_field = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id="sign-up-dlg__last-name-fld"]'))
	)
	last_name_input_field.send_keys('TestLastName')

	password_input_field = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id="sign-up-dlg__password-fld"]'))
	)
	password_input_field.send_keys('test_password')

	pass

# Clicks the age verification checkbox
@when('click the age certification')
def step_impl(context):
	certify_box_field = driver.find_element_by_class_name('jss754')

	certify_box_field.click()
	assert certify_box_field.is_selected(), 'Certify box selected'

# Clicks the submit button on the sign up form, fails if it is not enabled
@when('click the get started form button')
def step_impl(context):
	get_started_form_button = driver.find_element_by_css_selector('[data-test-id="sign-up-sign-up-button"]')
	is_enabled = get_started_form_button.is_enabled()

	get_started_form_button.click()
	assert is_enabled, 'Failed to click sign up submit button'

	

# Verifies that the page has been redirected to the user's home page after signing up
@then('we should be redirected to user home page')
def step_impl(context):
	wait = WebDriverWait(driver, 15)
	desired_url = "https://staging.padsplit.com/rooms-for-rent/"
	wait.until(lambda driver: driver.current_url == desired_url)

	assert driver.current_url==desired_url


###
# Logging out of a PadSplit account
###

# Verifies that the browser is currently signed into a PadSplit account
@given('we are signed into a PadSplit account')
def step_impl(context):
	try:
		log_out_button = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id="app-bar__log-out-item"]'))
		)
		pass
	except NoSuchElementException:
		assert False, "Not signed into an account"

# Hovers over the user's avatar and clicks the logout button
@when('we click the log out button')
def step_impl(context):
	action = ActionChains(driver);
	user_menu_hover_button = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id="app-bar__avatar-btn"]'))
	)
	action.move_to_element(user_menu_hover_button).perform()

	log_out_button = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id="app-bar__log-out-item"]'))
	)
	log_out_button.click()
	pass

# Verifies that the user has been logged out
@then('we should be logged out')
def step_impl(context):
	try:
		sign_in_button = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id="app-bar__sign-in-btn"]'))
	    )
		assert sign_in_button.is_displayed()
	except NoSuchElementException:
		assert False, "Unable to log out"


###
# Opening the PadSplit sign in form
###

# Presses the "Sign In" button on PadSplit's navigation bar
@when('we click the sign in button')
def step_impl(context):
	sign_in_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id="app-bar__sign-in-btn"]'))
    )
	sign_in_button.click();
	pass

# Verifies that the sign in container has opened
@then('the sign in dialog should appear')
def step_impl(context):
	try:
		sign_in_window = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id="sign-in-dlg"]'))
	    )
		assert sign_in_window.is_displayed()
	except NoSuchElementException:
		assert False, "No sign in dialog"

# Step used for readability in the .feature file - not fundamentally necessary (yet)
@given('the sign in form is open')
def step_impl(context):
	pass

# Inputs test data for the sign in form
@when('we fill out the sign in form')
def step_impl(context):
	email_input_field = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id="sign-in-dlg__email-fld"]'))
	)
	email_input_field.send_keys('testaccount@gmail.com')

	password_input_field = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id="sign-in-dlg__password-fld"]'))
	)
	password_input_field.send_keys('testpassword')

	pass

# Clicks the submit button on the sign in form, fails if it is not enabled
@when('click the sign in form button')
def step_impl(context):
	sign_in_form_button = driver.find_element_by_css_selector('[data-test-id="sign-in-sign-in-button"]')
	is_enabled = sign_in_form_button.is_enabled()
	
	sign_in_form_button.click()
	assert is_enabled, 'Failed to click sign in submit button'

# Verifies that the browser has been logged in
@then('we should be signed in')
def step_impl(context):
	user_avatar_button = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test-id="app-bar__avatar-btn"]'))
	)
	assert user_avatar_button.is_displayed(), 'Test account is not logged in'

