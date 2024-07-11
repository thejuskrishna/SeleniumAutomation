import unittest
from TestCases.BaseTest import BaseTest
from Pages.WalmartPage import WalmartPage
from TestCases.testlabel import testlabel

@testlabel('example', 'group0')
class TestWalmart(BaseTest):
  def setUp(self):
    super().setUp()

  def tearDown(self):
    super().tearDown()

  def test_load_walmart(self):
    walmart_page = WalmartPage(self.driver)
    walmart_page.go_to_walmart()
    walmart_page.verify_robot_human()

# if __name__ == '__main__':
#     unittest.main()

