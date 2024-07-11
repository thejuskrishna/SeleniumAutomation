from TestCases.BaseTest import BaseTest
from Pages.StayQriousPage import StayQriousPage

from TestCases.testlabel import testlabel

@testlabel('stayqrious', 'group1')
class TestStayQrious(BaseTest):
  def setUp(self):
    super().setUp()

  def tearDown(self):
    super().tearDown()

  def test_load_url(self):
    stay_qrious = StayQriousPage(self.driver)
    stay_qrious.go_to_website()
    stay_qrious.go_to_pricing()

