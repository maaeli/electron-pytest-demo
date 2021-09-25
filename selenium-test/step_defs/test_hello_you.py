import platform
from pathlib import PurePath
from selenium import webdriver
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

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


scenarios("../features/hello_you.feature")


@given("I have entered the app")
def enter_app(app):
    button = app.find_element_by_xpath("//button[text()='Click me']")
    button.click()


@when("I enter <my_name> in the input field")
def click_button(app, my_name):
    app.find_element_by_id("input-name").send_keys(my_name)


@then("the text 'Hello <my_name>' will be displayed")
def check_text_displayed(app, my_name):
    my_text = f"Hello {my_name}"
    body = app.find_element_by_tag_name("body")
    assert my_text in body.text