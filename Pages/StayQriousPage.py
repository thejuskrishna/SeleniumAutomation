from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
class StayQriousPage(BasePage):
  STAYQRIOUS_URL = "https://stayqrious.com/"
  PRICING_ELEMENT = (By.LINK_TEXT, "Pricing")
  APPLY_BUTTON = (By.CLASS_NAME, "MuiButton-label")

  def __init__(self, driver):
    self.driver = driver

  def go_to_website(self):
    self.open_url(self.STAYQRIOUS_URL)

  def go_to_pricing(self):
    self.click_element(self.PRICING_ELEMENT)
    self.scroll_to_element(self.APPLY_BUTTON)
