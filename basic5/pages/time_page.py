from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import Page

class TimePage(Page):
    HOUR_SEEKBAR = (AppiumBy.XPATH, '//android.widget.SeekBar[contains(@content-desc, "เลือกชั่วโมง")]')
    HOUR_TEXTBOX = (AppiumBy.XPATH, '//android.widget.EditText[contains(@text, "ชั่วโมง")]')
    MINUTE_TEXTBOX = (AppiumBy.XPATH, '//android.widget.EditText[contains(@text, "นาที")]')
    
    def input_hour(self, hour: str):
        self.double_click(*self.HOUR_SEEKBAR)
        self.send_keys(hour, *self.HOUR_TEXTBOX)

    def input_minute(self, minute: str):
        self.send_keys(minute, *self.MINUTE_TEXTBOX)

    def verify_time_picker(self, time: str):
        time_xpath = (AppiumBy.XPATH, '//*[contains(@text, "Hour")]')
        time_text = self.find_element(*time_xpath).get_attribute("text")
        assert time in time_text, "Time is not matched with right time"
    