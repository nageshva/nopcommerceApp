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
        testCases(Packag)
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
   