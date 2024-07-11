from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Resources.DataConfig import DataConfig

class BasePage:
  def __init__(self, driver):
    self.driver = driver

  def open_url(self, url):
    self.driver.get(url)

  def click_element(self, by_locator):
    WebDriverWait(self.driver, DataConfig.ELEMENT_WAIT_TIME).until(EC.visibility_of_element_located(by_locator)).click()

  def wait_for_element(self, by_locator):
    WebDriverWait(self.driver, DataConfig.LONG_WAIT_TIME).until(EC.visibility_of_element_located(by_locator))

  def enter_text(self, by_locator, text):
    WebDriverWait(self.driver, DataConfig.ELEMENT_WAIT_TIME).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

  def scroll_to_element(self, by_locator):
    element = self.driver.find_element(by_locator[0], by_locator[1])
    self.driver.execute_script("arguments[0].scrollIntoView();", element)

  def execute_script(self, javascript):
    self.driver.execute_script(javascript)