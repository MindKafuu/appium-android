from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import Page

class MainPage(Page):
    SUBMIT_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Submit"]')
    OK_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="OK"]')
    CALENDAR = (AppiumBy.XPATH, '//*[contains(@text, "Date")]')
    _OK_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="ตกลง"]')
    TIME_BUTTON = (AppiumBy.XPATH, '//*[contains(@text, "Hour")]')
    DROP_DOWN = (AppiumBy.XPATH, '//android.widget.Button[@index="6"]')

    def tap_submit_button(self):
        self.click(*self.SUBMIT_BUTTON)

    def tap_OK_button(self):
        self.click(*self.OK_BUTTON)

    def tap_calendar(self):
        self.click(*self.CALENDAR)

    def tap_ok(self):
        self.click(*self._OK_BUTTON)

    def tap_time_button(self):
        self.click(*self.TIME_BUTTON)

    def tap_drop_down(self):
        self.click(*self.DROP_DOWN)