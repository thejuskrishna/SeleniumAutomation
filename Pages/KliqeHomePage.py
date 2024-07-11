from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class KliqeHomePage(BasePage):
  KLIQE_URL = "https://kliqe.com"
  SIGN_IN = (By.CLASS_NAME, "signin")
  

  def __init__(self, driver):
    self.driver = driver
  def go_to_kliqe(self):
    return self.open_url(self.KLIQE_URL)

  def click_sign_in(self):
    self.click_element(self.SIGN_IN)
