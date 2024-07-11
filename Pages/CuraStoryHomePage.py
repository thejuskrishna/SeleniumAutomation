from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class CuraStoryHomePage(BasePage):
  CURA_STORY_URL = "https://curastory.co"
  ACCEPT_COOKIES = (By.LINK_TEXT, "Yes! I accept all cookies")
  LINK_TEXT = (By.LINK_TEXT, "Sign In")

  def __init__(self, driver):
    self.driver = driver
  def go_to_curastory(self):
    return self.open_url(self.CURA_STORY_URL)

  def accept_cookies(self):
    return self.click_element(self.ACCEPT_COOKIES)

  def click_sign_in(self):
    self.click_element(self.LINK_TEXT)
