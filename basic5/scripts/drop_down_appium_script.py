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

driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@index="6"]').click()

text = "Free"

driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="' + text + '"]').click()

drop_text = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@index="6"]').get_attribute("content-desc")

assert drop_text == text, "The option is not matched with " + text
