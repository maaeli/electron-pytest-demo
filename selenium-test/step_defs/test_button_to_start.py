import platform
from pathlib import PurePath
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    chrome_service = webdriver.chrome.service.Service(chrome_driver_path)
    chrome_service.start()

    options = webdriver.ChromeOptions()
    options.binary_location = str(electron_application_path)
    chrome_driver = webdriver.Remote(
        command_executor=chrome_service.service_url, options=options
    )
    yield chrome_driver
    chrome_driver.quit()
    chrome_service.stop()


scenarios("../features/button_to_start.feature")


@given("I have started the app")
def start_app(app):
    pass


@when("I click on the button 'Click me'")
def click_button(app):
    button = app.find_element(By.XPATH, "//button[text()='Click me']")
    button.click()


@then(parsers.parse("the text '{my_text}' will be displayed"))
def check_text_displayed(app, my_text):
    body = app.find_element(By.TAG_NAME, "body")
    assert my_text in body.text