from appium import webdriver
from app.application import Application
import pandas as pd

def before_feature(context, feature):
    for s in feature.scenarios:
        if 'test-data-from-excel' in s.tags:
            path_to_file = 'features/resources/mock_account_10.xlsx'
            df = pd.read_excel(path_to_file)
            example = next(sc.examples[0] for sc in feature.scenarios if sc.name == 'Logging in on app')
            test_table = example.table
            for row in df.itertuples(index=False):
                # for i in range(3):
                cell = (str(row[:][0]), str(row[:][1]))
                    # print(cell)
                test_table.add_row(cell)
        else:
            print("No mock data.")
 
def before_scenario(context, scenario):
    desired_cap = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "app": "D:/650018/Appium/basic5/app_binaries/app-debug_test.apk",
        "appPackage": "com.example.mobile_banking",
        "appActivity": "com.example.mobile_banking.MainActivity",
        "automationName": "UiAutomator2"
    }

    commnad_executor = "http://127.0.0.1:4723/wd/hub"
    context.driver = webdriver.Remote(commnad_executor, desired_cap)
    context.driver.implicitly_wait(5)
    context.app = Application(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()