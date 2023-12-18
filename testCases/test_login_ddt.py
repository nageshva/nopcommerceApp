import time

from selenium import webdriver
import pytest
from pageobjects.Loginpage import LoginPage
from utilties.readProperties import ReadConfig
from utilties.customLogger import LogGen
from utilties import XLUtilties


class Test_002_DDT_Login:
    baseURL=ReadConfig.getApplicationURL()
    path=".//testData/Logn_TestData.xlsx"
    logger=LogGen.loggen()

    def test_Login_DDT(self,setup):

        self.logger.info('** ** *** * Test_002_DDT_Login ** ** ** ** **')
        self.logger.info('** ** ** ** ** * Verifying Login DDT test ** **  ** **')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        self.rows=XLUtilties.getrowCount(self.path,'Sheet1')

        print('No of rows in excel sheet are:',self.rows)

        lst_status=[]

        for r in range(2,self.rows+1):
            self.username=XLUtilties.readData(self.path,'Sheet1',r,1)
            self.password = XLUtilties.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtilties.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)

            self.lp.clcikLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("**** failed ****")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
        print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")




