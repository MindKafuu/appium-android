from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "D:/650018/Appium/basic5/app_binaries/app-debug_test.apk",
    "appPackage": "com.example.mobile_banking",
    "appActivity": "com.example.mobile_banking.MainActivity",
    "automationName": "UiAutomator2"
}

commnad_executor = "http://127.0.0.1:4723/wd/hub"
driver = webdriver.Remote(commnad_executor, desired_cap)
driver.implicitly_wait(3)

check_box = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox[@index="9"]')
check_box.click()

assert bool(check_box.get_attribute("checked")) == True, "The option is not selected"

