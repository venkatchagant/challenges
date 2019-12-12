import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup



class Challenge3(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        #code to close webdriver
        self.driver.close()

    def test_challenge3(self):
        # code for our test steps
        self.driver.get("https://www.copart.com")

        html_copart = self.driver.find_element_by_id("tabTrending").get_attribute('innerHTML')



        soup = BeautifulSoup(html_copart, "html")

        for a in soup.find_all('a', href=True):
            if (a['href'].find("make") != -1  or a['href'].find("model") != -1) and not a['href'].find("category") != -1 :
                make = str(a)[str(a).index(">") + 1 : str(a).index("</a>")]
                print str(make) + " - " + a['href']



if __name__ == '__main__':
    unittest.main()