from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

desired_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "D:/650018/Appium/APK file/app-debug.apk",
    "appPackage": "com.example.mobile_banking",
    "appWaitActivity": "com.example.mobile_banking.MainActivity",
    "automationName": "UiAutomator2",
}

# Create the driver instance
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# Variables
# actions = ActionChains(driver)

def login(username, password):
    # username
    for i in range(3):
        driver.find_element_by_xpath(
            "//android.widget.EditText[@index='0']"
            ).click()
        driver.implicitly_wait(30)
    driver.find_element_by_xpath(
        "//android.widget.EditText[@index='0']"
        ).send_keys(username)

    # password
    for i in range(1):
        driver.find_element_by_xpath(
            "//android.widget.EditText[@index='1']"
            ).click()
        driver.implicitly_wait(30)
    driver.find_element_by_xpath(
        "//android.widget.EditText[@index='1']"
        ).send_keys(password)

    driver.find_element_by_xpath(
        "//android.widget.Button[@content-desc='เข้าสู่ระบบ']"
        ) .click()  
    
def pin_code(pin):
    # pin code
    for i in pin:
        driver.find_element_by_xpath(
            "//android.widget.Button[@content-desc='" + i + "']"
        ).click()
        
login("1000038", "12345678")
pin_code("111111")