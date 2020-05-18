# PYTEST With Python :

![python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)

pytest is a mature full-featured Python testing tool that helps you write better programs.

pytest is a framework that makes building simple and scalable tests easy. Tests are expressive and readable—no boilerplate code required. Get started in minutes with a small unit test or complex functional test for your application or library.

#### Pre Requisites

  - Making the project as :
    ```
    mkdir pytest-fixture-app
	cd pytest-fixture-app
    ```
  - Web Scraping installation:
     ```
     open command prompt type 
        pip install virtualenv
     create virtualenv
    	>>virtualenv venv
     we need to activate virtualenv for use
    	>>venv\scripts\activate
    ```
  - Run the following command in your command line:
    ```
    pip install -U pytest
    ```
  - Difference between @pytest.fixture and @pytest.yield_fixture in pytest
    * fixtures using the normal fixture decorator can use a yield statement to provide fixture values and execute teardown code, exactly like yield_fixture in previous versions. 
    * Marking functions as yield_fixture is still supported, but deprecated and should not be used in new code.
    * yield use the cleanup after the yield statement is run as a finalizer
    
  - Way of execute program as below :
     *  pytest
     *  pytest test_test_login_Testcase.py
     *  pytest -v -s 
     *  pytest -v -s login_test/test_Login_Testcase.py
     *  pytest -v -s login_test/test_Login_Testcase.py::test_login_by_gmail 
     *  pytest -v -s c:\SELENIUM\PYTEST\pytest-fixture-app

  - menaing -v, -s
    * -v : verbosity 
        
        You only have 3 different levels:

        * 0 (quiet): you just get the total numbers of tests executed and the global result
        * 1 (default): you get the same plus a dot for every successful test or a F for every failure
        * 2 (verbose): you get the help string of every test and the result
        
    * -s : Print all statement related to test case    