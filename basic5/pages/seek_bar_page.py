from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import Page

class SeekBar(Page):
    LEFT_SEEK_BAR = (AppiumBy.XPATH, '//android.widget.SeekBar[@index="0"]')
    RIGHT_SEEK_BAR = (AppiumBy.XPATH, '//android.widget.SeekBar[@index="1"]')

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

    def drag_seek_bar(self, left: str, right: str):
        left_seek_bar = self.find_element(*self.LEFT_SEEK_BAR)
        right_seek_bar = self.find_element(*self.RIGHT_SEEK_BAR)
        yAxis = left_seek_bar.location.get("y")

        startX = left_seek_bar.location.get("x")
        startY = right_seek_bar.location.get("x")

        moveToXDirectionAt = self.start_list[left] + startX
        _moveToXDirectionAt = self.stop_list[right] + startY

        if int(left) >= int(right_seek_bar.get_attribute("content-desc").split(", ")[1]):
            self.click_and_hold(_moveToXDirectionAt, yAxis, *self.RIGHT_SEEK_BAR)
            self.click_and_hold(moveToXDirectionAt, yAxis, *self.LEFT_SEEK_BAR)
        else:
            self.click_and_hold(moveToXDirectionAt, yAxis, *self.LEFT_SEEK_BAR)
            self.click_and_hold(_moveToXDirectionAt, yAxis, *self.RIGHT_SEEK_BAR)

    def verify_left_seek_bar(self, left: str):
        start_text = self.find_element(*self.LEFT_SEEK_BAR).get_attribute("content-desc").split(", ")[1]

        assert start_text == left, "The left " + start_text + " is not matched with " + str(left)

    def verify_right_seek_bar(self, right: str):
        stop_text = self.find_element(*self.RIGHT_SEEK_BAR).get_attribute("content-desc").split(", ")[1]

        assert stop_text == right, "The right " + stop_text + " is not matched with " + str(right)

