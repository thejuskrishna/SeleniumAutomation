import functools
import unittest

from tauk.config import TaukConfig
from tauk.listeners.unittest_listener import TaukListener
from tauk.tauk_webdriver import Tauk
from optparse import OptionParser


from Resources.DataConfig import DataConfig

class MyTestRunner(unittest.runner.TextTestRunner):
  def __init__(self, *args, **kwargs):
    """
    Append blacklist & whitelist attributes to TestRunner instance
    """

    super(MyTestRunner, self).__init__(*args, **kwargs)

  @classmethod
  def test_iter(cls, suite):
    """
    Iterate through test suites, and yield individual tests
    """
    for test in suite:
      if isinstance(test, unittest.TestSuite):
        for t in cls.test_iter(test):
          yield t
      else:
        yield test
  def run(self, testlist):
    suite = unittest.TestSuite()
    for test in self.test_iter(testlist):
      test_method = getattr(test, test._testMethodName)
      testlabels = getattr(test, "_labels", set())

      if DataConfig.include == '' and DataConfig.exclude == '' and (DataConfig.test != '' or DataConfig.test == 'all'):
        suite.addTest(test)
      if DataConfig.include in testlabels:
        suite.addTest(test)
      if DataConfig.exclude in testlabels:
        @functools.wraps(test_method)
        def skip_wrapper(*args, **kwargs):
          raise unittest.SkipTest('label exclusion')

        skip_wrapper.__unittest_skip__ = True
        skip_wrapper.__unittest_skip_why__ = 'label exclusion'

        setattr(test, test._testMethodName, skip_wrapper)
        suite.addTest(test)
    super(MyTestRunner, self).run(suite)
if __name__ == '__main__':
  parser = OptionParser()
  parser.add_option('-t', '--test', dest="test", help='Enter test to run the test or all to run all', default="all")
  parser.add_option('-c', '--cloud', dest="cloud", help='Cloud URL', default=False)
  parser.add_option('-b', '--browser', dest="browser", help='Browser', default="chrome")
  parser.add_option('-i', '--include', dest="include", help='Include Test Suite', default=False)
  parser.add_option('-e', '--exclude', dest="exclude", help='Exclude Test Suite', default=False)
  (option, arg) = parser.parse_args()

  #Setup desired capabilities from command line

  if option.browser == "chrome" or option.browser == "Chrome":
    DataConfig.BROWSER = "chrome"
  if option.browser == "firefox" or option.browser == "Firefox":
    DataConfig.BROWSER = "firefox"
  if hasattr(option, "cloud") and option.cloud != False:
    DataConfig.HOST_SERVER = option.cloud
  else:
    DataConfig.HOST_SERVER = "http://127.0.0.1:4723/wd/hub"

  if option.exclude != False:
    DataConfig.exclude = option.exclude
  if option.include != False:
    DataConfig.include = option.include

  # Tauk(TaukConfig(api_token=DataConfig.TAUK_API_TOKEN, project_id=DataConfig.TAUK_PROJECT_ID))
  loader = unittest.TestLoader()
  DataConfig.test = option.test
  if option.test == "all":
    suite = loader.discover("./", pattern="test*.py")
  else:
    suite = loader.discover("./", pattern=str(option.test) + ".py")
  alltests = unittest.TestSuite((suite))
  # unittest.TextTestRunner(resultclass=TaukListener, verbosity=2).run(alltests)
  runner = unittest.TextTestRunner()
  result = runner.run(alltests)
  print("Done")