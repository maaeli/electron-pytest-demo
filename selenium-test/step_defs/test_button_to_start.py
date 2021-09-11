import platform
from pathlib import PurePath
from selenium import webdriver
import pytest
from pytest_bdd import scenarios, given, when, then

this_file_as_path = PurePath(__file__)

if platform.system() == "Darwin":
    electron_application_path = PurePath(
        this_file_as_path.parents[2],
        "electron-demo",
        "out",
        "electron-demo-darwin-x64",
        "electron-demo.app",
        "Contents",
        "MacOS",
        "electron-demo",
    )
    chrome_driver_path = PurePath(
        this_file_as_path.parents[1],
        "chromedriver",
    )
elif platform.system() == "Linux":
    electron_application_path = PurePath(
        this_file_as_path.parents[2],
        "electron-demo",
        "out",
        "electron-demo-linux-x64",
        "electron-demo",
    )
    chrome_driver_path = PurePath(
        this_file_as_path.parents[1],
        "chromedriver",
    )
elif platform.system() == "Windows":
    electron_application_path = PurePath(
        this_file_as_path.parents[2],
        "electron-demo",
        "out",
        "electron-demo-win32-x64",
        "electron-demo.exe",
    )
    chrome_driver_path = PurePath(
        this_file_as_path.parents[1],
        "chromedriver.exe",
    )
else:
    raise Exception("No package location known for " + platform.system())


@pytest.fixture
def app():
    options = webdriver.ChromeOptions()
    options.binary_location = str(electron_application_path)
    chrome_driver = webdriver.Chrome(chrome_driver_path, options=options)
    yield chrome_driver
    chrome_driver.quit()


scenarios("../features/button_to_start.feature")


@given("I have started the app")
def start_app(app):
    pass


@when("I click on the button 'Click me'")
def click_button(app):
    button = app.find_element_by_xpath("//button[text()='Click me']")
    button.click()


@then("the text 'Hello World' will be displayed")
def check_text_displayed(app):
    body = app.find_element_by_tag_name("body")
    assert "Hello World!" in body.text