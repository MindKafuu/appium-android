from multiprocessing.sharedctypes import Value
from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

"""
Desired Capablilities
"""

desired_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "app": "C:/Users/chana/Downloads/com.flipkart.android.1500300.apk",
    "appPackage": "com.flipkart.android",
    "appWaitActivity": "com.flipkart.android.activity.FirstLaunchActivity",
}

# Create the driver instance
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# Variables
actions = ActionChains(driver)

# Functions
def find_language_element_by_xpath(number):
    element = driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[' + str(
            number) + ']/android.widget.RelativeLayout'
    )
    return element


def scroll(start, stop):
    actions.click_and_hold(find_language_element_by_xpath(start))
    actions.move_to_element(find_language_element_by_xpath(stop))
    actions.perform()

while(True):
    if (len(driver.find_elements_by_xpath("//android.widget.TextView[@text='English']")) > 0):
        driver.find_element_by_xpath("//android.widget.TextView[@text='English']").click()
        break
    else:
        scroll(7, 1)
    
"""
driver.find_element_by_id("com.flipkart.android:id/select_btn").click()

# Close popup
driver.find_element_by_id("com.flipkart.android:id/custom_back_icon").click()

# Interact with textbox
driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
).click()
driver.find_element_by_id(
    "com.flipkart.android:id/search_autoCompleteTextView"
).send_keys("nintendo switch")
"""

