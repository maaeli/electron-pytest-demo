import platform
from pathlib import Path, PurePath
from time import sleep
from selenium import webdriver


this_file_as_path = PurePath(Path.cwd(), __file__)


if platform.system() == "Darwin":
    electron_application_path = PurePath(
        this_file_as_path.parents[1],
        "electron-demo",
        "out",
        "electron-demo-darwin-x64",
        "electron-demo.app",
        "Contents",
        "MacOS",
        "electron-demo",
    )
    chrome_driver_path = PurePath(
        this_file_as_path.parent,
        "chromedriver",
    )
elif platform.system() == "Linux":
    electron_application_path = PurePath(
        this_file_as_path.parents[1],
        "electron-demo",
        "out",
        "electron-demo-linux-x64",
        "electron-demo",
    )
    chrome_driver_path = PurePath(
        this_file_as_path.parent,
        "chromedriver",
    )
elif platform.system() == "Windows":
    electron_application_path = PurePath(
        this_file_as_path.parents[1],
        "electron-demo",
        "out",
        "electron-demo-win32-x64",
        "electron-demo.exe",
    )
    chrome_driver_path = PurePath(
        this_file_as_path.parent,
        "chromedriver.exe",
    )
else:
    raise Exception("No package location known for " + platform.system())


options = webdriver.ChromeOptions()
options.binary_location = str(electron_application_path)
chrome_driver = webdriver.Chrome(chrome_driver_path, options=options)
sleep(5)
chrome_driver.quit()
