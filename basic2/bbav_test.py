from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

"""
Desired Capablilities
"""

desired_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:/Work/Python/Autoamtion Testing/Appium/APK file/app-debug.apk",
    "appPackage": "com.example.mobile_banking",
    "appWaitActivity": "com.example.mobile_banking.MainActivity",
    "automationName": "UiAutomator2",
}

# Create the driver instance
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# Variables
# actions = ActionChains(driver)

driver.find_element_by_xpath(
    "//android.widget.EditText[@index='0']"
    ).click()

# driver.find_element_by_xpath(
#     "//android.widget.EditText[@index='0']"
#     ).send_keys("1000038")

# actions.send_keys("1000038").perform()
# driver.find_element_by_xpath(
#     "//android.widget.EditText[@index='1']"
#     ).send_keys("12345678")
# driver.find_element_by_xpath(
#     "//android.widget.Button[@content-desc='เข้าสู่ระบบ']"
# ).click()
