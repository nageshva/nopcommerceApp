import time

from selenium import webdriver
import pytest
from pageobjects.Loginpage import LoginPage
from utilties.readProperties import ReadConfig
from utilties.customLogger import LogGen
from pageobjects.SearchCustomerPage import SearchCustmer
from pageobjects.AddcustomerPage import AddCustomer


class Test_SearchCustmerByEmail_004:
    baseurl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()   #Logger


    def test_searchCustomerByEmail(self,setup):
        self.logger.info("*********SearchCustomerByEmail_004********")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clcikLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by emailID **********")


        searchcust=SearchCustmer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)

        status = searchcust.searchCustmerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()

        assert True==status
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")











