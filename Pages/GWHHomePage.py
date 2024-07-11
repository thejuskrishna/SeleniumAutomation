from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
class GWHHomePage(BasePage):
  GWH_LOGIN_URL = "https://goodworkhub.com/login"
  GWH_EMAIL_ID = (By.ID, "register-email")
  GWH_PWD = (By.ID, "register-password")
  CLICK_LOGIN_BUTTON = (By.TAG_NAME, "button")
  def __init__(self, driver):
    self.driver = driver

  def go_to_goodworkhub(self):
    return self.open_url(self.GWH_LOGIN_URL)

  def enter_email_id(self):
    return self.enter_text(self.GWH_EMAIL_ID, "thejuskrishna@gmail.com")

  def enter_pwd(self):
    return self.enter_text(self.GWH_PWD, "1234!")

  def click_login_button(self):
    return self.click_element(self.CLICK_LOGIN_BUTTON)