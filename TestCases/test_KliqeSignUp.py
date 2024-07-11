import unittest
from time import sleep
from TestCases.BaseTest import BaseTest
from Pages.KliqeSignUpPage import KliqeSignUpPage
from TestCases.testlabel import testlabel

@testlabel('example', 'group0')
class TestCuraStory(BaseTest):
  def setUp(self):
    super().setUp()

  def tearDown(self):
    super().tearDown()

  def test_load_kliqesignup(self):
    kliqe_signup = KliqeSignUpPage(self.driver)
    kliqe_signup.go_to_kliqe()
    kliqe_signup.click_sign_up()
    sleep(3)
    print(self.driver.current_url)
    kliqe_signup.enter_name()
    kliqe_signup.enter_email()
    kliqe_signup.enter_password()
    kliqe_signup.click_checkbox()
    kliqe_signup.click_next()
    sleep(5)
    print(self.driver.current_url)

if __name__ == '__main__':
    unittest.main()

