from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.calendar_page import Calendar
from pages.time_page import TimePage
from pages.seek_bar_page import SeekBar
from pages.drop_down_page import DropDown

class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.calendar_page = Calendar(driver)
        self.time_page = TimePage(driver)
        self.seek_bar_page = SeekBar(driver)
        self.drop_down_page = DropDown(driver)
