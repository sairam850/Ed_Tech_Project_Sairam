from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import BasePage
from Data.TestData import GuviStoreData
from Configuration.conftest import driver
from time import sleep
import pytest

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
def test_reload_url(driver):
    driver.get(GuviStoreData.guvi_url)
    base_page = BasePage(driver)

    # asserting expected vs actual url
    assert base_page.fetch_url() == "https://www.guvi.in/"
    print("Success: Test Case Passed for Reload URL")

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
# Test Case to Validate Title
def test_validate_title(driver):
    driver.get(GuviStoreData.guvi_url)
    base_page = BasePage(driver)

    # asserting expected vs actual title
    assert base_page.fetch_title() == "GUVI | Learn to code in your native language"
    print("Success:Test Case Passed for Valid Title")

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
# Test Case to Validate Login Button Visibility
def test_login_visibility(driver):
    driver.get(GuviStoreData.guvi_url)
    login_page = LoginPage(driver)

    # asserting the Login Button Visibility as True
    assert login_page.login_visibility() == True
    print("Success: Test Case Passed for Login Visibility")

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
# Test Case to Validate Sign-up Button Visibility
def test_sign_up_visibility(driver):
    driver.get(GuviStoreData.guvi_url)
    login_page = LoginPage(driver)

    # asserting the Signup Visibility as True
    assert login_page.sign_up_visibility() == True
    print("SUCCESS :Test Case Passed for sign_up_visibility")

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
# Test Case to Validate Signin Page after Signup
def test_signin_signup(driver):
    driver.get(GuviStoreData.guvi_url)
    login_page = LoginPage(driver)
    login_page.sign_up()
    login_page.login_signup()

    # asserting expected vs actual URL
    assert "https://www.guvi.in/sign-in/" == driver.current_url
    print("Success:Test Case Passed for Login Using SignUp")

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
# Test Case for Valid Login Credentials
def test_valid_login(driver):
    driver.get(GuviStoreData.guvi_url)
    base_page = BasePage(driver)
    login_page = LoginPage(driver)
    login_page.click_login()
    login_page.enter_username(GuviStoreData.username_valid)
    login_page.enter_password(GuviStoreData.password_valid)
    login_page.click_guvi_login()
    sleep(5)

    # asserting expected vs actual URL
    assert base_page.fetch_url()== "https://www.guvi.in/courses/?current_tab=myCourses"
    print("Success:Test Case Passed for Valid Username and Password")

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
# Test Case for Valid Username and Invalid Password
def test_invalid_password_login(driver):
    driver.get(GuviStoreData.guvi_url)
    login_page = LoginPage(driver)
    login_page.click_login()
    login_page.enter_username(GuviStoreData.username_valid)
    login_page.enter_password(GuviStoreData.password_invalid)
    login_page.click_login()

    # Asserting Error Message to be True
    assert login_page.error_message1() == True
    print("Success:Test Case Passed for Valid Username and Password")

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
# Test Case for Invalid Email and Valid Password
def test_invalid_email_login(driver):
    driver.get(GuviStoreData.guvi_url)
    login_page = LoginPage(driver)
    login_page.click_login()
    login_page.enter_username(GuviStoreData.username_invalid)
    login_page.enter_password(GuviStoreData.password_valid)
    login_page.click_login()

    # Asserting Error Message to be True
    assert login_page.error_message1() == True
    print("Success:Test Case Passed for Valid Username and Password")

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
# Test Case for Empty Username and Valid Password
def test_empty_username(driver):
    driver.get(GuviStoreData.guvi_url)
    login_page = LoginPage(driver)
    login_page.click_login()
    login_page.enter_username(GuviStoreData.empty_username)
    login_page.enter_password(GuviStoreData.password_valid)
    login_page.click_login()

    # asserting expected vs actual URL
    assert "https://www.guvi.in/sign-in/" == driver.current_url
    print("Success:Test Case Passed for Empty Username and Valid Password")

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
# Test Case for Valid Username and Empty Password
def test_empty_password(driver):
    driver.get(GuviStoreData.guvi_url)
    login_page = LoginPage(driver)
    login_page.click_login()
    login_page.enter_username(GuviStoreData.username_valid)
    login_page.enter_password(GuviStoreData.empty_password)
    login_page.click_login()

    # Asserting Error Message to be True
    assert login_page.error_message2() == True
    print("Success:Test Case Passed for Valid Username and Empty Password")

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
# Test Case for Empty Username and Empty Password
def test_empty_username_password(driver):
    driver.get(GuviStoreData.guvi_url)
    login_page = LoginPage(driver)
    login_page.click_login()
    login_page.enter_username(GuviStoreData.empty_username)
    login_page.enter_password(GuviStoreData.empty_password)
    login_page.click_login()

    # Asserting Error Message to be True
    assert login_page.error_message2() == True
    print("Success:Test Case Passed for Verify for Empty Username and Empty Password")

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
# Test Case for Invalid Username and Invalid Password
def test_invalid_email_invalid_password(driver):
    driver.get(GuviStoreData.guvi_url)
    login_page = LoginPage(driver)
    login_page.click_login()
    login_page.enter_username(GuviStoreData.username_invalid)
    login_page.enter_password(GuviStoreData.password_invalid)
    login_page.click_login()

    # Asserting Error Message to be True
    assert login_page.error_message1() == True
    print("Success:Test Case Passed for Verify for InValid Username and ValidPassword")

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
# Test Case to Validate List of Menu Items
def test_menu_displayed(driver):
    driver.get(GuviStoreData.guvi_url)
    login_page = LoginPage(driver)

    # Asserting Display Menu Item to be True
    assert login_page.menu_displayed() == True
    print("Success:Test Case Passed for Menu Item Displayed")

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
# Test Case for Logout Functionality
def test_logout_button_work(driver):
    driver.get(GuviStoreData.guvi_url)
    base_page = BasePage(driver)
    login_page = LoginPage(driver)
    login_page.click_login()
    login_page.enter_username(GuviStoreData.username_valid)
    login_page.enter_password(GuviStoreData.password_valid)
    login_page.click_guvi_login()
    sleep(5)
    login_page.guvi_image()
    login_page.click_logout()
    sleep(3)

    # asserting expected vs actual URL
    assert base_page.fetch_url()== "https://www.guvi.in/"
    print("Success:Test Case Passed for Logout Functionality is working Properly")

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
# Test Case to Validate GUVI Assistant Present
def test_guviassistant(driver):
    driver.get(GuviStoreData.guvi_url)
    login_page = LoginPage(driver)
    sleep(5)

    #Asserting Dobby Assistant to be true
    assert login_page.guvi_assistant() == True
    print("Success:Test Case Passed for Menu Item Displayed")












