from selenium import webdriver
import pytest
from pageobjects.Loginpage import LoginPage
from utilties.readProperties import ReadConfig
from utilties.customLogger import LogGen


class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_homePage_Title(self,setup):

        self.logger.info(('** ** *** * Test_001_Login ** ** ** ** **'))
        self.logger.info(('** **** * Verifying Home Page Title ** ** ** * **'))
        self.driver=setup
        self.driver.get(self.baseURL)
        actual_title=self.driver.title


        if actual_title =='Your store. Login':
            assert True
            self.driver.close()
            self.logger.info(('** ** **  ** * Home Page title test is passed ** ** ** ** **'))
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePage_Title.png")
            self.driver.close()
            self.logger.error(('** ** ** ** * Home Page title test is failed ** * ** ** '))
            assert False

    def test_Login(self,setup):

        self.logger.info(('** ** ** ** ** * Verifying Login test ** **  ** **'))
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)

        self.lp.clcikLogin()

        if self.driver.title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info(('** ** ** ** ** * Login test passed ** **  ** **'))

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_Login.png")
            self.driver.close()
            self.logger.error(('** ** ** ** ** * Login test Failed ** **  ** **'))
            assert False










