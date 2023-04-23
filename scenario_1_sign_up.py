
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


# SCENARIO 1: Sign-up into Goodreads website
# Description: This task involves automating the sign-up process on the Goodreads website,
# followed by logging in with the created account (another scenario 2).
class Sign_up(unittest.TestCase):

	SIGNUP_BUTTON = (By.LINK_TEXT, "Sign up with email")
	YOUR_NAME_FIELD = (By.ID, "ap_customer_name")
	EMAIL_FIELD = (By.XPATH, '//*[@id="ap_email"]')
	PASSWORD_FIELD = (By.ID, "ap_password")
	RE_ENTER_PASSWORD_FIELD = (By.ID, "ap_password_check")
	CREATE_ACCOUNT_BUTTON = (By.ID, "continue")

	def setUp(self) -> None:
		self.driver = webdriver.Chrome()
		self.driver.get("https://www.goodreads.com/") # step a
		self.driver.maximize_window()
		self.driver.find_element(*self.SIGNUP_BUTTON).click() # step b
		self.driver.implicitly_wait(3)

	def tearDown(self) -> None:
		self.driver.quit()

	# Test 1 : c. Fill out the sign-up form with the required information
		# fill "Your name" field with valid credentials
		# fill "Email" field with valid credentials
		# fill "Password" field with valid credentials
		# fill "Re-enter password" field with valid credentials
		# click "Create account" button
		# check if the message "Important message: You indicated you're a new customer,
	# but an account already exists with the email address" is displayed.
	def test_1(self):
		self.driver.find_element(*self.YOUR_NAME_FIELD).send_keys('Zoicas Ramona')
		self.driver.find_element(*self.EMAIL_FIELD).send_keys('ramona.vascul@yahoo.com')
		self.driver.find_element(*self.PASSWORD_FIELD).send_keys('lovelyday123')
		self.driver.find_element(*self.RE_ENTER_PASSWORD_FIELD).send_keys('lovelyday123')
		self.driver.find_element(*self.CREATE_ACCOUNT_BUTTON).click()
		self.driver.find_element(By.XPATH, '//*[@id="auth-warning-message-box"]/div/div/ul/li/span').is_displayed()



