from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
class CuraStoryLoginPage(BasePage):
  CURA_LOGIN_URL = "https://app.curastory.co/login"
  EMAIL_TEXTBOX = (By.NAME, "email")
  CLICK_LOGIN_BUTTON = (By.TAG_NAME, "button")

  def __init__(self, driver):
    self.driver = driver
  def enter_email_id(self):
    return self.enter_text(self.EMAIL_TEXTBOX, "tk@kriya.live")

  def click_login_button(self):
    return self.click_element(self.CLICK_LOGIN_BUTTON)