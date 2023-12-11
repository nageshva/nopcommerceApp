from selenium import webdriver
import pytest
from pageobjects.Loginpage import LoginPage


class Test_001_Login:
    baseURL="https://admin-demo.nopcommerce.com/"
    username="admin@yourstore.com"
    password="admin"

    def test_homePage_Title(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        actual_title=self.driver.title


        if actual_title =='Your store. Lgin':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePage_Title.png")
            self.driver.close()
            assert False

    def test_Login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)

        self.lp.clcikLogin()

        if self.driver.title=="Dashboard / npCommerce administration":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_Login.png")

            self.driver.close()
            assert False










