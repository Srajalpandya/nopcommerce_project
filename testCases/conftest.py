from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    return driver

def pytest_addoption(parser):   #This will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the browser value to setup method
    return request.config.getoption("--browser")

################# Pytest HTML Report #####################

# It is hook for adding environment info to html report
def pytest_configure(config):
    #config._metadata['project  Name'] = 'nop commerce'
    #config._metadata['Module Name'] = 'Customers'
    #config._metadata['Tester'] = 'Srajal Pandya'
    config._metadata = {
        "Project Name": "nop commerce",
        "Module Name": "Customer",
        "Tester": "Srajal Pandya"
    }

# It is hook for delete//modify environment info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_Home", None)
    metadata.pop("Plugins", None)

