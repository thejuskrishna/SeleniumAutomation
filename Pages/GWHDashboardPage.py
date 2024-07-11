from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
class GWHDashboardPage(BasePage):
  GWH_DASHBOARD_AVATAR = (By.CLASS_NAME, "avatar-content")

  def __init__(self, driver):
    self.driver = driver

  def verify_landingpage(self):
    return self.wait_for_element(self.GWH_DASHBOARD_AVATAR)
