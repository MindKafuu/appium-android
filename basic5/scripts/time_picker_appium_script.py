from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains

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
actions = ActionChains(driver)

driver.find_element(AppiumBy.XPATH, '//*[contains(@text, "Hour")]').click()

hour_seek_bar = driver.find_element(AppiumBy.XPATH, '//android.widget.SeekBar[contains(@content-desc, "เลือกชั่วโมง")]')
actions.double_click(hour_seek_bar).perform()
hour_text = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[contains(@text, "ชั่วโมง")]')
hour_text.clear()
hour_text.send_keys("11")

minute_text = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[contains(@text, "นาที")]')
minute_text.clear()
minute_text.send_keys("11")

driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="ตกลง"]').click()

time_text = driver.find_element(AppiumBy.XPATH, '//*[contains(@text, "Hour")]').get_attribute("text")

assert "11:11" in time_text, "Time is not matched with right time"

