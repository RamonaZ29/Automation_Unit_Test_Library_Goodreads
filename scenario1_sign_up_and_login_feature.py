
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from webdriver_manager.chrome import ChromeDriverManager

# SCENARIO 1: Sign-up and log in into Goodreads website
# Description: This task involves automating the sign-up process(test 1) on the Goodreads website,
# followed by logging in with the created account (test2).

class Sign_up_and_login(unittest.TestCase):

	SIGNUP_BUTTON = (By.LINK_TEXT, "Sign up with email")
	YOUR_NAME_FIELD = (By.ID, "ap_customer_name")
	EMAIL_FIELD = (By.XPATH, '//*[@id="ap_email"]')
	PASSWORD_FIELD = (By.ID, "ap_password")
	RE_ENTER_PASSWORD_FIELD = (By.ID, "ap_password_check")
	CREATE_ACCOUNT_BUTTON = (By.ID, "continue")
	CREATE_ACCOUNT_EXIST_MESSAGE = (By.XPATH, '//div[@id="auth-warning-message-box"]/div')
	HOMEPAGE_SIGN_IN_BUTTON = (By.LINK_TEXT, "Sign In")
	SIGN_IN_WITH_EMAIL_BUTTON = (By.XPATH, '//*[@id="choices"]/div/a[2]/button')
	LOGINPAGE_SIGN_IN_BUTTON = (By.ID, "signInSubmit")
	PROFILE_ICON = (By.XPATH, '//div/a/span/img[@class="circularIcon circularIcon--border"]')
	PROFILE_OPTION = (By.LINK_TEXT, "Profile")

	def setUp(self) -> None:
		self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
		self.driver.get("https://www.goodreads.com/") # step a
		self.driver.maximize_window()
		self.driver.implicitly_wait(3)

	def tearDown(self) -> None:
		self.driver.quit()

	# Test 1 : c. Fill out the sign-up form with the required information
		# c1. fill "Your name" field with valid credentials
		# c2. fill "Email" field with valid credentials
		# c3. fill "Password" field with valid credentials
		# c4. fill "Re-enter password" field with valid credentials
		# d. click "Create account" button
		# e. check if the message "Important message: You indicated you're a new customer,
	# but an account already exists with the email address" is displayed.

	def test_1_check_create_account_user_exists(self):
		# nr = random.randint(1,99999999999999)
		self.driver.find_element(*self.SIGNUP_BUTTON).click() # step b
		self.driver.find_element(*self.YOUR_NAME_FIELD).send_keys('Zoicas Ramona')
		self.driver.find_element(*self.EMAIL_FIELD).send_keys(f'ramona.vascul@yahoo.com') #aici inainte de @{nr}
		self.driver.find_element(*self.PASSWORD_FIELD).send_keys('lovelyday123')
		self.driver.find_element(*self.RE_ENTER_PASSWORD_FIELD).send_keys('lovelyday123')
		self.driver.find_element(*self.CREATE_ACCOUNT_BUTTON).click()
		assert self.driver.find_element(*self.CREATE_ACCOUNT_EXIST_MESSAGE).is_displayed() == True

	# Test 2: Check Sign in feature with valid credentials
	# f. click on "sign in with email" button on sign-in page
	# g1. enter in the "email" field the created credentials
	# g2. enter in the "password" field the created credentials
	# h. click "Sign in" button
	# i1. click on your profile icon
	# i2. click on "Profile" option
	# i3. Verify that the login is successful by checking the user dashboard

	def test_2_login_into_the_application(self):
			time.sleep(3)
			self.driver.find_element(*self.HOMEPAGE_SIGN_IN_BUTTON).click()
			self.driver.find_element(*self.SIGN_IN_WITH_EMAIL_BUTTON).click()
			self.driver.find_element(*self.EMAIL_FIELD).send_keys("ramona.vascul@yahoo.com")
			self.driver.find_element(*self.PASSWORD_FIELD).send_keys("lovelyday123")
			self.driver.find_element(*self.LOGINPAGE_SIGN_IN_BUTTON).click()
			self.driver.find_element(*self.PROFILE_ICON).click()
			self.driver.find_element(*self.PROFILE_OPTION).click()
			current_url = self.driver.current_url
			assert "zoicas-ramona" in current_url


