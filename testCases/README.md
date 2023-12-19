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


   