from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    #First locate the objects/Web elements

    textbox_username_id="Email"
    textbox_password_id='Password'
    button_login_xpath="//button[normalize-space()='Log in']"
    link_logout_linktext="Logout"


  #Driver Initilization
    def __init__(self,driver):
        self.driver=driver


 #Write Actions methods for each Object/Web Elements
    def setUsername(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clcikLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()

