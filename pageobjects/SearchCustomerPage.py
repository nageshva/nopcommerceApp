from selenium.webdriver.common.by import By


class SearchCustmer():
    # First locate the objects/Web elements
    # Search customer page
    txtsearchBoxXpth="//div[@class='search-text']"
    txtEmailId = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    # Driver Initilization

    def __init__(self, driver):
        self.driver = driver

    # Write Actions methods for each Object/Web Elements
    def Search(self):
        self.driver.find_element(By.XPATH,self.txtsearchBoxXpth).click()


    def setEmail(self, Email):
        self.driver.find_element(By.ID, self.txtEmailId).clear()
        self.driver.find_element(By.ID, self.txtEmailId).send_keys(Email)

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))
    def getNoOfColumns(self):
        cols = len(self.driver.find_element(By.XPATH, self.tableColumns_xpath))
        return int(cols)

    def searchCustmerByEmail(self, Email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[2]").text
            if emailid == Email:
                flag = True
                break
        return flag

    def searchCustmerByName(self,Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag


