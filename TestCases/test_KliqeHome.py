import unittest
from time import sleep
from TestCases.BaseTest import BaseTest
from Pages.KliqeHomePage import KliqeHomePage
from Pages.CuraStoryLoginPage import CuraStoryLoginPage
from TestCases.testlabel import testlabel

@testlabel('example', 'group0')
class TestCuraStory(BaseTest):
  def setUp(self):
    super().setUp()

  def tearDown(self):
    super().tearDown()

  def test_load_kliqe(self):
    kliqe_home = KliqeHomePage(self.driver)
    kliqe_home.go_to_kliqe()
    kliqe_home.click_sign_in()
    sleep(3)
    print(self.driver.current_url)

if __name__ == '__main__':
    unittest.main()

