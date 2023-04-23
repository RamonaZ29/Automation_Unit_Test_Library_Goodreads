
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


# SCENARIO 2: Log-in into Goodreads website
# Description :This task involves automating logging in with the created account at scenario 1.

class Login(unittest.TestCase):

    # atribute de la Test 1
    HOMEPAGE_SIGN_IN_BUTTON = (By.LINK_TEXT, "Sign In")
    SIGN_IN_WITH_EMAIL_BUTTON = (By.XPATH, '//*[@id="choices"]/div/a[2]/button')
    EMAIL_FIELD = (By.ID,"ap_email")
    PASSWORD_FIELD = (By.ID,"ap_password")
    LOGINPAGE_SIGN_IN_BUTTON = (By.ID, "signInSubmit")
    DASHBOARD_LOGIN_PROOF = (By.XPATH, "/html/body/div[2]/div/header/div[1]/div/div[3]/ul/li[5]/div/a/span/img")

    #atribute de la Test 2
    SEARCH_BAR = (By.XPATH, '/html/body/div[2]/div/header/div[1]/div/div[2]/form/input[1]')
    SEARCH_ICON = (By.XPATH, '/html/body/div[2]/div/header/div[1]/div/div[2]/form/button')
    SEARCH_RESULTS = (By.XPATH, '/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/h3')
    DESIRED_BOOK = (By.XPATH, '/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]/a/span')
    WANT_TO_READ_BUTTON = (By.XPATH, '//*[@id="__next"]/div/main/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/button')

    # atribute de la Test 3
    # RATING_STARS =
    WRITE_A_REVIEW_BUTTON = (By.XPATH, '//*[@id="__next"]/div/main/div[1]/div[1]/div/div[2]/div[3]/div/span/a')
    WHAT_DID_YOU_THINK_BOX = (By.XPATH, '//*[@id="review_review_usertext"]')
    POST_BUTTON = (By.XPATH, '//*[@id="review_submit_for_58537332"]')
    REVIEW_PROOF = (By.XPATH, '//*[@id="freeTextContainerreview5503775947"]')





    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.goodreads.com/")  # step a
        self.driver.maximize_window()
        self.driver.find_element(*self.HOMEPAGE_SIGN_IN_BUTTON).click()  # step f
        self.driver.implicitly_wait(3)

    def tearDown(self) -> None:
        self.driver.quit()

    # Test 1: Check Sign in feature with valid credentials
        # click on "sign in with email" button on sign-in page
        # g1. enter in the "email" field the created credentials
        # g2. enter in the "password" field the created credentials
        # h. click "Sign in" button
        # i. Verify that the login is successful by checking the user dashboard ##???

    def test_1(self):
        self.driver.find_element(*self.SIGN_IN_WITH_EMAIL_BUTTON).click()
        self.driver.find_element(*self.EMAIL_FIELD).send_keys("ramona.vascul@yahoo.com")
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys("lovelyday123") # aici se opreste
        self.driver.find_element(*self.LOGINPAGE_SIGN_IN_BUTTON).click()

        # username_label = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/header/div[1]/div/div[3]/ul/li[5]/'
        #                                                     'div/a/span/img').text
        # containing_message = 'Zoicas Ramona'
        # assert containing_message in username_label, f'The actual text does not contain {containing_message}'
        # assert "Zoicas Ramona" in username_label, f'The expected url is : "Zoicas Ramona" but went {username_label}'
        # self.assertEqual(username_label.text, "Zoicas Ramona") #nu stiu cum e corect?

        #Test 2: Search and add a book to the "Want to read" section (apartine de Scenario 3)
        # Description: This task involves automating the search for a book on the Goodreads
        # website and adding it to the user's "Want to Read" shelf.
            # b'. Click on the search bar
            # c'. Enter the book name in the search bar
            # d'. Click on "Search" button
            # e'. Verify that the search results are displayed
            # f'. Click on the desired book from the search results
            # g'. Verify that the book page is loaded
            # h'. Click on "Want to Read" button on the book page
            # i'. Verify that the book is added to the "Want to Read" shelf on the user's dashboard

    def test_2(self):
        self.driver.find_element(*self.SEARCH_BAR).click()
        self.driver.find_element(*self.SEARCH_BAR).send_keys("the myth of normal")
        self.driver.find_element(*self.SEARCH_ICON).click()
        actual_result= self.driver.find_element(*self.SEARCH_RESULTS).text

        expected_result = "Page 1 of about 102 results"
        assert expected_result in actual_result, f"Results are different!" #??

        self.driver.find_element(*self.DESIRED_BOOK).click()

        current_url = self.driver.current_url
        expected_url = 'https://www.goodreads.com/book/show/58537332-the-myth-of-normal?from_search=true&from_srp=true&qid=PrtNG0HLs0&rank=1'
        assert current_url == expected_url, \
            f' The expected url is {expected_url} but went: {current_url}'

        self.driver.find_element(*self.WANT_TO_READ_BUTTON).click()
         #??? nu stiu pasul : Verify that the book is added to the "Want to Read" shelf on the user's dashboard

    # Test 3: Search and add a book review on Goodreads website
    # Description: This task involves automating the search for a book on the Goodreads
    # website and adding a review to it.
        # b'. Click on the search bar # idem Test 2 pana la g'
        # c'. Enter the book name in the search bar
        # d'. Click on "Search" button
        # e'. Verify that the search results are displayed
        # f'. Click on the desired book from the search results
        # g'. Verify that the book page is loaded
        # h''. Rate the book with stars form 1 to 5 #???
        # h1''. Click on "Write a review" button on the book page
        # i''. Enter the review text in the review box
        # j''. Click on "Save"/ "Post" button
        # k''. Verify that the review is added to the book page

    def test_3(self):
        self.driver.find_element(*self.SEARCH_BAR).click()
        self.driver.find_element(*self.SEARCH_BAR).send_keys("the myth of normal")
        self.driver.find_element(*self.SEARCH_ICON).click()
        actual_result= self.driver.find_element(*self.SEARCH_RESULTS).text

        expected_result = "Page 1 of about 102 results"
        assert expected_result in actual_result, f"Results are different!" #??

        self.driver.find_element(*self.DESIRED_BOOK).click()

        current_url = self.driver.current_url
        expected_url = 'https://www.goodreads.com/book/show/58537332-the-myth-of-normal?from_search=true&from_srp=true&qid=PrtNG0HLs0&rank=1'
        assert current_url == expected_url, \
            f' The expected url is {expected_url} but went: {current_url}'

        # pasul h'' -nu stiu?

        self.driver.find_element(*self.WRITE_A_REVIEW_BUTTON).click()
        self.driver.find_element(*self.WHAT_DID_YOU_THINK_BOX).send_keys("This is a thought-provoking and insightful book.")
        self.driver.find_element(*self.POST_BUTTON).click()

        actual_review = self.driver.find_element(*self.REVIEW_PROOF).text
        expected_review = "This is a thought-provoking and insightful book."
        assert expected_review == actual_review, f'The expected review is {expected_review}, but the actual is {actual_review}.'






















