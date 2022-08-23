from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

"""
Desired Capablilities
"""

desired_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:/Work/Python/Autoamtion Testing/Appium/APK file/io.flutter.demo.gallery_2021-05-26.apk",
    "appPackage": "io.flutter.demo.gallery",
    "appWaitActivity": "io.flutter.demo.gallery.MainActivity",
    "automationName": "UiAutomator2",
}

# Create the driver instance
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# Variables
actions = ActionChains(driver)

driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View/android.widget.HorizontalScrollView"
).click()
driver.find_element_by_xpath(
    "//android.view.View[@content-desc='Compose']"
).click()
driver.find_element_by_xpath(
    "//android.widget.EditText[@text='Subject']"
).click()
driver.find_element_by_xpath(
    "//android.widget.EditText[@text='Subject']"
).send_keys("test")

driver.find_element_by_accessibility_id

    
# username_text_element.click()