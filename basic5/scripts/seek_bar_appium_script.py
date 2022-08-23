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

left_seek_bar = driver.find_element(AppiumBy.XPATH, '//android.widget.SeekBar[@index="0"]')
right_seek_bar = driver.find_element(AppiumBy.XPATH, '//android.widget.SeekBar[@index="1"]')

yAxis = left_seek_bar.location.get("y")

startX = left_seek_bar.location.get("x")
endX = left_seek_bar.size.get("width")

startY = right_seek_bar.location.get("x")
endY = right_seek_bar.size.get("width")

start_list = {
    "0": -150,
    "20": 0,
    "40": 150,
    "60": 300,
    "80": 500,
    "100": 669
}

stop_list = {
    "0": -1200,
    "20": -1100,
    "40": -850,
    "60": -700,
    "80": -500,
    "100": 0
}

start = 20
stop = 60

moveToXDirectionAt = start_list[str(start)] + startX
_moveToXDirectionAt = stop_list[str(stop)] + startY

if start >= int(right_seek_bar.get_attribute("content-desc").split(", ")[1]):
    actions.click_and_hold(right_seek_bar).move_by_offset(_moveToXDirectionAt, yAxis).release().perform()
    actions.click_and_hold(left_seek_bar).move_by_offset(moveToXDirectionAt, yAxis).release().perform()
else:
    actions.click_and_hold(left_seek_bar).move_by_offset(moveToXDirectionAt, yAxis).release().perform()
    actions.click_and_hold(right_seek_bar).move_by_offset(_moveToXDirectionAt, yAxis).release().perform()

print(_moveToXDirectionAt, startY)

start_text = left_seek_bar.get_attribute("content-desc").split(", ")[1]
stop_text = right_seek_bar.get_attribute("content-desc").split(", ")[1]

assert start_text == start, "The left " + start_text + " is not matched with " + str(start)
assert stop_text == stop, "The right " + stop_text + " is not matched with " + str(stop)