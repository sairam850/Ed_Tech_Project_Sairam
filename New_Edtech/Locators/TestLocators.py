"""
This locator file contains all the web locators like ID, CLASS NAME, XPATH etc.,
"""

class Locators:
    # login page
    login_click_url = 'login-btn' #ID
    username_locator = 'email' # ID
    password_locator = 'password' # ID
    guvi_login = '//a[@id = "login-btn" and text() = "Login"]' #XPATH
    sign_up = '//a[@class = "⭐️rawbli-0 bg-green-500 hover:bg-green-600 text-white font-normal py-2 px-4 rounded text-base min-h-8 h-8 align-middle mr-2 text-nowrap"]' #XPATH
    login_sign_up = '//a[@href = "/sign-in/" and text() = "Login"]' #XPATH
    dobby_text = 'chateleon-container-gif-0' #ID
    courses = '//*[@href = "/courses/" and text() = "Courses"]' #XPATH
    liveclasses= 'liveclasseslink' #ID
    practice = 'practiceslink'  #ID
    resources = 'resourceslink' #ID
    products = 'solutionslink'  #ID
    guvi_image_click = '//div[@id = "dropdown_container"]'  # XPATH
    guvi_signout = '//li[div[@id = "dropdown_contents"]]'  # XPath
    error_message1 = '//div[contains(text(), "Incorrect Email or Password")]' # XPath
    error_message2 = '//div[contains(text(), "Hey, Did you forgot your password? Try again.")]' # XPath


