## Selenium Hybrid Framework
(Python,Selenium,Pytest,Page Object Model,HTML Reports)

**Step1:Create a new Project & Install Required Packages/Plugins**
 
 - Selenium:Selenium Libraries
 - Pytest: Python UnitTest Framework
 - Pytest-html:PyTest HTML Reports
 - Pytest-xdist:Run Tests Parallel
 - Openpyxl: MS Excel Support
 - Allure-Pytest: Allure reports Generation

**Step2:Create Folder Structure**

   **Project Name**
         
        |
      
        PageObjects(Package)
        |
        testCases(Package)
        |
        utilities(Package)
        |
        TestData(Folder)
        |
        Configurations(Folder)
        |
        Logs(Folder)
        |
        Screenshots(Folder)
        |
        Reports(Folder)
        |
        Run.bat
**Step3:Automating Login Test Case**
   
    3.1:Create Login Page Object Class under"pageObjects"
    3.2:Create LoginTest Under "testCases"
    3.3:Create confest.py under "testCases"
**Step4:Capture screenshot on failures**

    4.1:Update Login test with screenshot under"testCases"
**Step5:Read common values from ini.file**

    5.1:Add "config.ini"file in Configurations folder.
    5.2:Create "readProperties.py" utilty file under utilties package to read common data
    5.3:Replace hardcoded values in Login test case

**Step6:Adding logs to test case**

    6.1:Add customLogger.py under utilites package 
    6.2:Add logs to Login test case

**Step7:Run tests on desired Browsers/Cross Browser/Parallel**

    7.1:Update contest.py with required Fixers which will accept command line arguement(Browser)
    7.2:Pass browser name as arguement in command line

**To Run tests on desired browser**
   
pytest -s -v testCases/test_login.py --browser chrome

pytest -s -v testCases/test_login.py --browser firefox

pytest -s -v testCases/test_login.py --browser ie

**To Run tests parallel**

pytest -s -v -n=3 testCases/test_login.py --browser chrome

pytest -s -v -n=3 testCases/test_login.py --browser firefox

pytest -s -v -n=3 testCases/test_login.py --browser ie


**Step8:Genearate pytest HTML Reports**

    8.1:To generate HTML report run below command
    pytest -s -v -n=3 --html=Reports.html testCases/test_login.py -browser chrome

**Step9:Automating Data Driven TestCases**

    9.1:Prepare test data in excel sheet,place the excel file inside the testdata folder
    9.2:Create" Excelutils.py utility class under utilities package.
    9.3:Create Logindata driven test case under testcases
    9.4:Run the test case

**Step10:Add new test cases if any**

**Step11:Grouping Tests**

     11.1:Grouping markers(Add markers to every test method)
     @pytest.mark.sanity
     @pytest.mark.smoke
     @pytest.mark.regression
     
     11.2:To run as a group ,run this command

     pytest -s -v -m regression --html=Reports.html testCases/test_login.py --browser chrome

**Step12:Push the code to git & github repository**

    12.1:git status
    12.2:git add .
    12.3:git commit -m "Your commit message here"
    12.4:git push origin <branch_name>


   

