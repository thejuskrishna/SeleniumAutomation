import time
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class KliqeSignUpPage(BasePage):
  KLIQE_URL = "https://kliqe.com"
  SIGN_UP = (By.CLASS_NAME, "signup")
  FULLNAME = (By.ID, "signup_username")
  EMAIL = (By.ID, "signup_email")
  PASSWORD = (By.ID, "signup_password")
  REMEMBER_JS = 'document.getElementById("signup_remember").click();'
  CLICK_NEXT_JS = 'document.getElementsByClassName("signup-buttons")[0].firstChild.click();'
  

  def __init__(self, driver):
    self.driver = driver
  def go_to_kliqe(self):
    return self.open_url(self.KLIQE_URL)

  def click_sign_up(self):
    self.click_element(self.SIGN_UP)

  def enter_name(self):
    self.enter_text(self.FULLNAME, "Thejus Krishna")
  
  def enter_email(self):
    ts = int(time.time()*1000)
    email_id = "tk+" + str(ts)  + "@kriya.live"
    self.enter_text(self.EMAIL, email_id)

  def enter_password(self):
    self.enter_text(self.PASSWORD, "1234!")

  def click_checkbox(self):
    self.execute_script(self.REMEMBER_JS)

  def click_next(self):
    self.execute_script(self.CLICK_NEXT_JS)
    
