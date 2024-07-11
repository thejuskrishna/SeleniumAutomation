from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
class WalmartPage(BasePage):
  WALMART_URL = "https://walmart.com"
  ROBOT_HUMAN = (By.ID, "ld_modalTitle_0")
  def __init__(self, driver):
    self.driver = driver
  def go_to_walmart(self):
    return self.open_url(self.WALMART_URL)

  def verify_robot_human(self):
    return self.wait_for_element(self.ROBOT_HUMAN)
t