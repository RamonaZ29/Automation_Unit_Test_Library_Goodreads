from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from webdriver_manager.chrome import ChromeDriverManager

# SCENARIO 2: Search ,add a book to the "Want to read" section and leave a review on Goodreads website
# Description :This task involves automating logging in with the created account at scenario 1(in setup),
# search for a book, add it on "Want to read" section and leave a review

class Search_book(unittest.TestCase):

    # atribute din setup
    HOMEPAGE_SIGN_IN_BUTTON = (By.LINK_TEXT, "Sign In")
    EMAIL_FIELD = (By.ID,"ap_email")
    PASSWORD_FIELD = (By.ID,"ap_password")
    #atribute de la Test 1
    SEARCH_BAR = (By.XPATH, '//input[@class="searchBox__input searchBox__input--navbar"]')
    SEARCH_ICON = (By.XPATH, '//button[@type="submit" and @class="searchBox__icon--magnifyingGlass gr-iconButton searchBox__icon searchBox__icon--navbar"] ')
    SEARCH_RESULTS = (By.XPATH, '//h3[@class="searchSubNavContainer"]')
    DESIRED_BOOK = (By.XPATH, '//span[text()="The Myth of Normal: Trauma, Illness, and Healing in a Toxic Culture"]/parent::a')
    WANT_TO_READ_BUTTON = (By.XPATH, '//span[text()="Want to read"]/parent::button[@aria-label="Tap to shelve book as want to read"]')
    WANT_TO_READ_CHECK_BOOK = (By.XPATH,'//a[@title="The Myth of Normal: Trauma, Illness, and Healing in a Toxic Culture"]')
    # atribute de la Test 2
    WRITE_A_REVIEW_BUTTON = (By.LINK_TEXT,"Write a review")
    WHAT_DID_YOU_THINK_BOX = (By.ID,"review_review_usertext")
    POST_BUTTON = (By.ID,'id="review_submit_for_58537332"')
    REVIEW_PROOF = (By.XPATH, '//div[contains(text(),"This is a thought-provoking and insightful book.")]')
    SIGN_IN_WITH_EMAIL_BUTTON = (By.XPATH, '//*[@id="choices"]/div/a[2]/button')
    LOGINPAGE_SIGN_IN_BUTTON = (By.ID, "signInSubmit")
    MY_BOOKS = (By.LINK_TEXT,"My Books")
    RATE_BOOK = (By.XPATH,'//button[@aria-label="Rate 5 out of 5"]')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.get("https://www.goodreads.com/")
        self.driver.maximize_window()
        self.driver.find_element(*self.HOMEPAGE_SIGN_IN_BUTTON).click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(*self.SIGN_IN_WITH_EMAIL_BUTTON).click()
        self.driver.find_element(*self.EMAIL_FIELD).send_keys("ramona.vascul@yahoo.com")
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys("lovelyday123")
        self.driver.find_element(*self.LOGINPAGE_SIGN_IN_BUTTON).click()

    def tearDown(self) -> None:
        self.driver.quit()

        #Test 1: Search and add a book to the "Want to read" section
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
        # (we need to click "My Books" section to be able to check on dashbboard

    def test_search_and_add_book_to_wish_list(self):
        self.driver.find_element(*self.SEARCH_BAR).click() #b'
        self.driver.find_element(*self.SEARCH_BAR).send_keys("the myth of normal") #c'
        self.driver.find_element(*self.SEARCH_ICON).click() #d'
        results= self.driver.find_element(*self.SEARCH_RESULTS).text # e'
        number_of_returned_books = results[results.index("r")-4:results.index("r")].replace(" ","") #e'
        assert int(number_of_returned_books)>0, f"Search did not return any result!" #e'
        self.driver.find_element(*self.DESIRED_BOOK).click() #f'
        current_url = self.driver.current_url #g'
        assert "58537332" in current_url #g'
        self.driver.find_elements(*self.WANT_TO_READ_BUTTON)[0].click() #h'
        self.driver.find_element(*self.MY_BOOKS).click() # i'
        assert "The Myth of Normal" in self.driver.find_element(*self.WANT_TO_READ_CHECK_BOOK).text #i'

    # Test 2: Search and add a book review on Goodreads website
    # Description: This task involves automating the search for a book on the Goodreads
    # website and adding a review to it.
        # b'. Click on the search bar # OBS! from b'->g' steps are the same as in Test1
        # c'. Enter the book name in the search bar
        # d'. Click on "Search" button
        # e'. Verify that the search results are displayed
        # f'. Click on the desired book from the search results
        # g'. Verify that the book page is loaded
        # h''. Rate the book with stars form 1 to 5 (this is a mandatory step to be able to leave a review)
        # h1''. Click on "Write a review" button on the book page
        # i''. Enter the review text in the review box
        # j''. Click on "Save"/ "Post" button
        # k''. Verify that the review is added to the book page

    def test_add_review_to_book(self):
        self.driver.find_element(*self.SEARCH_BAR).click() #b'
        self.driver.find_element(*self.SEARCH_BAR).send_keys("the myth of normal") #c'
        self.driver.find_element(*self.SEARCH_ICON).click() #d'
        results= self.driver.find_element(*self.SEARCH_RESULTS).text # e'
        number_of_returned_books = results[results.index("r")-4:results.index("r")].replace(" ","") #e'
        assert int(number_of_returned_books)>0, f"Search did not return any result!" #e'
        self.driver.find_element(*self.DESIRED_BOOK).click() #f'
        current_url = self.driver.current_url #g'
        assert "58537332" in current_url #g'
        self.driver.find_elements(*self.RATE_BOOK)[0].click() #h''
        self.driver.find_element(*self.WRITE_A_REVIEW_BUTTON).click() #h1''
        self.driver.find_element(*self.WHAT_DID_YOU_THINK_BOX).send_keys\
            ("This is a thought-provoking and insightful book.") #i''
        self.driver.find_element(*self.POST_BUTTON).click() #j''
        actual_review = self.driver.find_element(*self.REVIEW_PROOF).text #k''
        expected_review = "This is a thought-provoking and insightful book." #k''
        assert expected_review == actual_review, f'The expected review is {expected_review}, ' \
                                                 f'but the actual is {actual_review}.'#k''




