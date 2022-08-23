import subprocess
from selenium.webdriver.common.action_chains import ActionChains

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        e = self.find_element(*locator)
        e.click()

    def input(self, text, *locator):
        e = self.find_element(*locator)
        e.clear()
        # print("adb -s emulator-5554 shell input text '" + text + "'")
        subprocess.call("adb -s emulator-5554 shell input text '" + text + "'", shell=True)

    def send_keys(self, text, *locator):
        e = self.find_element(*locator)
        e.click()
        e.clear()
        e.send_keys(text)

    def scroll(self, *points):
        self.actions.click_and_hold(self.find_element(points[0], points[1]))
        self.actions.move_to_element(self.find_element(points[2], points[3]))
        self.actions.perform()

    def double_click(self, *locator):
        e = self.find_element(*locator)
        self.actions.double_click(e).perform()

    def click_and_hold(self, posX, posY, *locator):
        e = self.find_element(*locator)
        self.actions.click_and_hold(e).move_by_offset(posX, posY).release().perform()