import unittest
from selenium import webdriver

from Resources.DataConfig import DataConfig

class BaseTest(unittest.TestCase):
  def setUp(self):
    if DataConfig.BROWSER == "chrome":
      self.driver = webdriver.Chrome(DataConfig.CHROME_DRIVER_PATH)
      self.driver.maximize_window()
      # Tauk.register_driver(self.driver, unittestcase=self)
    if DataConfig.BROWSER == "firefox":
      self.driver = webdriver.Firefox(executable_path=DataConfig.GECKO_DRIVER_PATH)
      self.driver.maximize_window()
      # Tauk.register_driver(self.driver, unittestcase=self)

  def tearDown(self):
    self.driver.quit()