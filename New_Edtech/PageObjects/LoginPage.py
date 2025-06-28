"""
Perform the Login of GUVI Button
GUVI Login URL https://www.guvi.in/
1. Reloading URL
2. Validate Title of Web Page
3. Verify visibility and clickability of login button
4. Verify visibility and clickability of signup button
5. Verify Navigation to Signin page via Signup button
6. Verify Login with Valid Credentials
7. Verify Login with Invalid Credentials
8. Verify Menu Items such as Courses, Live Classes and Practice are Displayed
9. Verify Dobby Assistant visible on Web Page
10. Verify Logout functionality
"""
# import all necessary dependencies
from selenium.webdriver.common.by import By
from Locators.TestLocators import Locators
from PageObjects.HomePage import BasePage


class LoginPage(BasePage):
    # Storing all the Locators
    USERNAME_INPUT = (By.ID, Locators.username_locator)
    PASSWORD_INPUT = (By.ID, Locators.password_locator)
    LOGIN_BUTTON = (By.ID, Locators.login_click_url)
    LOGOUT_BUTTON = (By.XPATH, Locators.guvi_signout)
    GUVI_IMAGE = (By.XPATH,Locators.guvi_image_click)
    SIGN_UP = (By.XPATH,Locators.sign_up)
    LOGIN_SIGN_UP = (By.XPATH,Locators.login_sign_up)
    ERROR_MESSAGE1 = (By.XPATH,Locators.error_message1)
    ERROR_MESSAGE2 = (By.XPATH, Locators.error_message2)
    COURSES = (By.XPATH,Locators.courses)
    LIVECLASSES = (By.ID,Locators.liveclasses)
    PRACTICE = (By.ID,Locators.practice)
    RESOURCES = (By.ID,Locators.resources)
    PRODUCTS = (By.ID,Locators.products)
    DOBBY = (By.ID,Locators.dobby_text)
    GUVI_LOGIN = (By.XPATH,Locators.guvi_login)

    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def click_logout(self):
        self.click(self.LOGOUT_BUTTON)

    def guvi_image(self):
        self.click(self.GUVI_IMAGE)

    def sign_up(self):
        self.click(self.SIGN_UP)

    def login_signup(self):
        self.click(self.LOGIN_SIGN_UP)

    def click_guvi_login(self):
        self.click(self.GUVI_LOGIN)


    # Verify for Visibility for Login Button
    def login_visibility(self):
        self.is_visible(self.LOGIN_BUTTON)
        self.is_clickable(self.LOGIN_BUTTON)
        self.click(self.LOGIN_BUTTON)

    # Verify for Visibility for Signup button
    def sign_up_visibility(self):
        self.is_visible(self.SIGN_UP)
        self.is_clickable(self.SIGN_UP)
        self.click(self.SIGN_UP)

    # Verify for Error Message Display for Invalid Credentials
    def error_message1(self):
        error_message21 = self.find_element(self.ERROR_MESSAGE1)
        if error_message21.is_displayed() and error_message21.is_enabled():
            return True
        else:
            return False

    # Verify for Error Message Display for Invalid Credentials
    def error_message2(self):
        error_message22 = self.find_element(self.ERROR_MESSAGE2)
        if error_message22.is_displayed() and error_message22.is_enabled():
            return True
        else:
            return False

    # Verify for Menu_Items_Displayed
    def menu_displayed(self):
        courses_verify = self.find_element(self.COURSES)
        livelink_verify = self.find_element(self.LIVECLASSES)
        practice_verify = self.find_element(self.PRACTICE)
        resource_verify = self.find_element(self.RESOURCES)
        products_verify = self.find_element(self.PRODUCTS)

        if courses_verify.is_displayed() and livelink_verify.is_displayed() and practice_verify.is_displayed() and resource_verify.is_displayed() and products_verify.is_displayed():
            return True
        else:
            return False

    # Verify for Visibility for GUVI Assistant
    def guvi_assistant(self):
        dobby_text = self.find_element(self.DOBBY)
        if dobby_text.is_displayed():
            return True
        else:
            return False























