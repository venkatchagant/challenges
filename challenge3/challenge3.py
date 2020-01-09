import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from bs4 import beautifulsoup



class Challenge3(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.get("https://www.copart.com")

    def tearDown(self):
        #code to close webdriver
        self.driver.close()

    def test_challenge3forloop(self):
        # code for our test steps


        #html_copart = self.driver.find_element_by_id("tabTrending").get_attribute('innerHTML')

        self.assertIn("Copart", self.driver.title)
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")
        for element in elements:
            print element.text + ":" + element.get_attribute("href")



        # soup = beautifulsoup(html_copart, "html")
        #
        # for a in soup.find_all('a', href=True):
        #     if (a['href'].find("make") != -1  or a['href'].find("model") != -1) and not a['href'].find("category") != -1 :
        #         make = str(a)[str(a).index(">") + 1 : str(a).index("</a>")]
        #         print str(make) + " - " + a['href']

    def test_challenge3whileloop(self):
        # code for our test steps
        #self.driver.get("https://www.copart.com")

        # html_copart = self.driver.find_element_by_id("tabTrending").get_attribute('innerHTML')

        self.assertIn("Copart", self.driver.title)
        #elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")
        elements = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]/../div[3]//a")
        print len(elements)

        i = 0
        while(i < len(elements) ):
            print elements[i].text + ":" + elements[i].get_attribute("href")

            i +=1

# bonu 4: help.sling.com    search roku
#  //*[@id=["channelList"]//img

#print elements[i].get_attribute("src") + ":" + elements[i].get_attribute("alt")

if __name__ == '__main__':
    unittest.main()