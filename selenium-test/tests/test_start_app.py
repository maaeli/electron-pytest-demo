import platform
from pathlib import PurePath
from time import sleep
import pytest
from selenium import webdriver

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


def test_start_app():
    options = webdriver.ChromeOptions()
    options.binary_location = str(electron_application_path)
    chrome_driver = webdriver.Chrome(chrome_driver_path, options=options)
    sleep(1)
    body = chrome_driver.find_element_by_tag_name("body")
    assert "💖 Hello World!" in body.text
    chrome_driver.quit()


@pytest.mark.xfail
def test_hello_maaeli():
    options = webdriver.ChromeOptions()
    options.binary_location = str(electron_application_path)
    chrome_driver = webdriver.Chrome(chrome_driver_path, options=options)
    sleep(1)
    body = chrome_driver.find_element_by_tag_name("body")
    assert "💖 Hello Maaeli!" in body.text
    chrome_driver.quit()
