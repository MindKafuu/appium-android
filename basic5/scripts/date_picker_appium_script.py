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

month_dict = {
    'มกราคม': 1,
    'กุมภาพันธ์': 2,
    'มีนาคม': 3,
    'เมษายน': 4,
    'พฤษภาคม': 5,
    'มิถุนายน': 6,
    'กรกฎาคม': 7,
    'สิงหาคม': 8,
    'กันยายน': 9,
    'ตุลาคม': 10,
    'พฤศจิกายน': 11,
    'ธันวาคม': 12
}


driver.find_element(AppiumBy.XPATH, '//*[contains(@text, "Date")]').click()

month_button = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@index="3"]')
while(True):
    if month_dict[month_button.get_attribute("content-desc").split(" ")[1]] - 1 == 0:
        break
    else:
        month_button.click()

driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="เลือกปี"]').click()

while(True):
    if len(driver.find_elements(AppiumBy.XPATH, '//android.view.View[@content-desc="2002"]')) > 0:
        driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="2002"]').click()
        break
    else:
        e = driver.find_element(AppiumBy.XPATH, '//android.view.View[@index="3"]')
        if (int(e.get_attribute("content-desc")) > 2002):
            actions.click_and_hold(driver.find_element(AppiumBy.XPATH, '//android.view.View[@index="3"]'))
            actions.move_to_element(driver.find_element(AppiumBy.XPATH, '//android.view.View[@index="11"]'))
            actions.perform()
        else:
            actions.click_and_hold(driver.find_element(AppiumBy.XPATH, '//android.view.View[@index="11"]'))
            actions.move_to_element(driver.find_element(AppiumBy.XPATH, '//android.view.View[@index="3"]'))
            actions.perform()

driver.find_element(AppiumBy.XPATH, "//*[contains(@content-desc, '17, วัน')]").click()

driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="ตกลง"]').click()

date_text = driver.find_element(AppiumBy.XPATH, '//*[contains(@text, "Date")]').get_attribute("text")

assert "17 Dec, 2002" in date_text, "Date is not matched with the right date."