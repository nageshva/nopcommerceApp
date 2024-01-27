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

    @pytest.mark.regression
    def test_homePage_Title(self,setup):

        self.logger.info('** ** *** * Test_001_Login ** ** ** ** **')
        self.logger.info('** **** * Verifying Home Page Title ** ** ** * **')
        self.driver=setup
        self.driver.get(self.baseURL)
        actual_title=self.driver.title


        if actual_title =='Your store. Login':
            assert True
            self.driver.close()
            self.logger.info('** ** **  ** * Home Page title test is passed ** ** ** ** **')
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePage_Title.png")
            self.driver.close()
            self.logger.error('** ** ** ** * Home Page title test is failed ** * ** ** ')
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self,setup):

        self.logger.info('** ** ** ** ** * Verifying Login test ** **  ** **')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)

        self.lp.clcikLogin()

        if self.driver.title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info('** ** ** ** ** * Login test passed ** **  ** **')

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_Login.png")
            self.driver.close()
            self.logger.error('** ** ** ** ** * Login test Failed ** **  ** **')
            assert False
    @pytest.mark.smoke
    def test_Login_Negative(self, setup):

        self.logger.info('** ** ** ** ** * Verifying Login test with invalid details ** **  ** **')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername("hari@gmail.com")
        self.lp.setPassword("jajiri123")

        self.lp.clcikLogin()

        if self.lp.error_msg_xpath=="Login was unsuccessful. Please correct the errors and try again." :
            assert True

            self.logger.info('** ** ** ** ** * Negative test is passed ** **  ** **')
            self.driver.close()



















