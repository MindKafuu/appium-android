import subprocess
from appium import webdriver
from requests import patch
from selenium.webdriver.common.by import By

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
driver.implicitly_wait(30)

username = driver.find_element(By.XPATH, '//android.widget.EditText[@index="0"]')
username.click()
subprocess.call("adb -s emulator-5554 shell input text '1'", shell=True)

password_textbox = driver.find_element(By.XPATH, "//android.widget.EditText[@index='1']")
password_textbox.click()
subprocess.call("adb -+...s emulator-5554 shell input text '1'", shell=True)

driver.find_element(By.XPATH, "//android.widget.Button[@content-desc='Submit']").click()

try:
    assert len(driver.find_elements(By.XPATH, "//android.view.View[@content-desc='กรอกข้อมูลถูก เข้าสู้ระบบนะจ๊ะ']")) > 0, "Incorrect account or password"
    print("successful")
except AssertionError as e:
    print(e)

# assert "กรอกข้อมูลถูก เข้าสู้ระบบนะจ๊ะ" in text, "Incorrect account or password"

driver.find_element(By.ACCESSIBILITY_ID, "OK").click()


