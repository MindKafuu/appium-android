from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import Page

class Calendar(Page):
    GREATER_THAN_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@index="3"]')
    PICK_YEAR = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="เลือกปี"]')
    TOP_ELEMENT = (AppiumBy.XPATH, '//android.view.View[@index="3"]')
    POINTS_DOWN = (AppiumBy.XPATH, '//android.view.View[@index="3"]', AppiumBy.XPATH, '//android.view.View[@index="11"]')
    POINTS_UP = (AppiumBy.XPATH, '//android.view.View[@index="11"]', AppiumBy.XPATH, '//android.view.View[@index="3"]')

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
    'ธันวาคม': 0
}

    def select_month(self, month: str):
        month_button = self.find_element(*self.GREATER_THAN_BUTTON)
        while(True):
            if self.month_dict[month_button.get_attribute("content-desc").split(" ")[1]] - 1 == self.month_dict[month]:
                break
            else:
                month_button.click()

    def select_year(self, year: str):
        selected_year = (AppiumBy.XPATH, '//android.view.View[@content-desc="' + year + '"]')
        self.click(*self.PICK_YEAR)
        while(True):
            if len(self.find_elements(*selected_year)) > 0:
                self.click(*selected_year)
                break
            else:
                top = self.find_element(*self.TOP_ELEMENT)
                if (int(top.get_attribute("content-desc")) > int(year)):
                    self.scroll(*self.POINTS_DOWN)

                else:
                    self.scroll(*self.POINTS_UP)

    def select_day(self, day: str):
        day = (AppiumBy.XPATH, "//*[contains(@content-desc, '" + day + ", วัน')]")
        self.click(*day)

    def verify_date_picker(self, text: str):
        date_xpath = (AppiumBy.XPATH, '//*[contains(@text, "Date")]')
        date_text = self.find_element(*date_xpath).get_attribute("text")
        assert text in date_text, "Date is not matched with the right date."


