import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class Challenge2(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome("../challenges/chromedriver")

    def tearDown(self):
        #code to close webdriver
        self.driver.close()

    def test_challenge2(self):
        # code for our test steps
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        self.driver.find_element_by_xpath("//input[@id='input-search']").send_keys("exotics")

        search_button = EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-lightblue marginleft15']"))

        wait(self.driver, 40).until(search_button)

        #wait(self.driver, 60)

        self.driver.find_element_by_xpath("//button[@class='btn btn-lightblue marginleft15']").click()

        element_present = EC.presence_of_element_located((By.XPATH, "//input[@class='form-control input-sm']" ))

        wait(self.driver, 20).until(element_present)

        list_of_cars = self.driver.find_element_by_xpath("//table[@id='serverSideDataTable']").text

        #print list_of_cars

        self.assertIn("PORSCHE",list_of_cars)


if __name__ == '__main__':
    unittest.main()