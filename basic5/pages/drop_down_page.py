from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import Page

class DropDown(Page):
    DROP_DOWN = (AppiumBy.XPATH, '//android.widget.Button[@index="6"]')

    def select_option(self, option: str):
        option_xpath = (AppiumBy.XPATH, '//android.view.View[@content-desc="' + option + '"]')
        self.click(*option_xpath)

    def verify_drop_down(self, option: str):
        drop_text = self.find_element(*self.DROP_DOWN).get_attribute("content-desc")
        
        assert drop_text == option, "The option is not matched with " + option