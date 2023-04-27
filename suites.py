import unittest
# from unittest import TestCase
import HtmlTestRunner #(instalat din python packages: html-testRunner,html-testRunner1005D)
from scenario1_sign_up_and_login_feature import Sign_up_and_login
from scenario2_search_book_and_add_review import Search_book

class TestSuite(unittest.TestCase): # pentru ca am importat toata libraria, trebuie sa o specificam in fata clasei parinte

		def test_suite(self): # numele metodei este predefinit si NU trebuie schimbat
				teste_de_rulat = unittest.TestSuite() # am instantiat un obiect al clasei TestSuite numit teste_de_rulat
									# prin intermediul acestui obiect vom accesa metoda addTests
									# metoda addTests primeste ca si parametru o lista de teste care se doreste a fi executate
									# testele vor fi separate prin virgula
									# teste_de_rular.addTest([]) -> apelare fara parametru
				teste_de_rulat.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Sign_up_and_login)
				 ,
							unittest.defaultTestLoader.loadTestsFromTestCase(Search_book)

																 						])

				runner = HtmlTestRunner.HTMLTestRunner(
						combine_reports=True, # vrem sa ne genereze un singur raport pentru toate clasele
						report_title="Test Execution Report",
						report_name= "Test Results"
				)

				runner.run(teste_de_rulat)