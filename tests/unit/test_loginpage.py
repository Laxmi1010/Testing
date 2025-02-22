import pytest
from Pages.login_page import LoginPage
from utils.excel_reader import get_data_from_excel

# Load test data from Excel
test_data = get_data_from_excel("login_data.xlsx", "Sheet1")

@pytest.mark.parametrize("username, password", test_data)
def test_login(setup, username, password):
    driver = setup
    login_page = LoginPage(driver)
    
    login_page.login(username, password)
    print("Current URL after login:", driver.current_url)

    # Example assertion: Check if login was successful
    assert "logged-in-successfully" in driver.current_url.lower(), "Login failed"


#@pytest.mark.parametrize is used in PyTest for data-driven testing, 
# allowing a test function to run multiple times with different inputs.