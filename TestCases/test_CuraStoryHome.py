import unittest
from time import sleep
from TestCases.BaseTest import BaseTest
from Pages.CuraStoryHomePage import CuraStoryHomePage
from Pages.CuraStoryLoginPage import CuraStoryLoginPage
from TestCases.testlabel import testlabel

@testlabel('example', 'group0')
class TestCuraStory(BaseTest):
  def setUp(self):
    super().setUp()

  def tearDown(self):
    super().tearDown()

  def test_load_gwh(self):
    curastory_page = CuraStoryHomePage(self.driver)
    curastory_page.go_to_curastory()
    curastory_page.accept_cookies()
    curastory_page.click_sign_in()
    sleep(3)

    self.driver.switch_to.window(self.driver.window_handles[1])
    print(self.driver.current_url)

# if __name__ == '__main__':
#     unittest.main()

