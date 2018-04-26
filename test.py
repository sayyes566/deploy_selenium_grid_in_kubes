from selenium import webdriver
import unittest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys, argparse

class SearchText(unittest.TestCase):
   def setUp(self):
        self.test_url=args.testurl
        print( 'test url = '+ self.test_url)
        print( 'webdriver url = http://'+ args.driverip+ ':4444/wd/hub')
        # create a new session
        self.chrome = webdriver.Remote(
            command_executor='http://' + args.driverip + ':4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        self.chrome.get(self.test_url )
   def test_search_by_text(self):
        #lists = self.chrome.find_elements_by_class_name("w10")
        #no=len(lists)
        title=self.chrome.title
        self.assertIn('Hello', title)
   def tearDown(self):
        # close the browser window
        self.chrome.quit()
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--driverip', default='My web driver ip')
    parser.add_argument('--testurl', default='My test url')
    parser.add_argument('unittest_args', nargs='*')
    args = parser.parse_args()
    sys.argv[1:] = args.unittest_args
    unittest.main()

