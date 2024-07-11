import unittest
from time import sleep
from TestCases.BaseTest import BaseTest
from Pages.GWHHomePage import GWHHomePage
from Pages.GWHDashboardPage import GWHDashboardPage
from TestCases.testlabel import testlabel

@testlabel('example', 'group0')
class TestGWHLanding(BaseTest):
  def setUp(self):
    super().setUp()

  def tearDown(self):
    super().tearDown()

  def test_load_gwh(self):
    gwh_page = GWHHomePage(self.driver)
    gwh_page.go_to_goodworkhub()
    sleep(3)
    print(self.driver.current_url)
    gwh_page.enter_email_id()
    gwh_page.enter_pwd()
    gwh_page.click_login_button()

    gwh_dashboard = GWHDashboardPage(self.driver)
    gwh_dashboard.verify_landingpage()
    print(self.driver.current_url)

# if __name__ == '__main__':
#     unittest.main()

