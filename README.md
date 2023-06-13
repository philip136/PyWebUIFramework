# PyWebUIFramework
This framework is needed for simple work with Selenium.

To start working with framework you have to write the following code:
```python
from browser.py_quality_services import PyQualityServices

browser = PyQualityServices.get_browser()
```
This line of code opens a browser, you can override the type of browser.
You have to create a folder called `resources`. The folder have to contain a `settings.json` file.
Example:
```json
{
  "browserName" : "chrome",
  "isRemote": false,
  "remoteConnectionUrl": "http://localhost:4444/wd/hub",
  "isElementHighlightEnabled" : true,

  "driverSettings": {
    "chrome": {
      "webDriverVersion": "latest",
      "capabilities": {
        "enableVNC": true
      },
      "options": {
        "intl.accept_languages": "en",
        "safebrowsing.enabled": "true",
        "profile.default_content_settings.popups": "0",
        "disable-popup-blocking": "true",
        "download.prompt_for_download": "false",
        "download.default_directory": "path_to_download_folder"
      },
      "pageLoadStrategy": "Normal",
      "startArguments": []
    },
    "firefox": {
      "webDriverVersion": "latest",
      "capabilities": {
        "enableVNC": true
      },
      "options": {
        "intl.accept_languages": "en",
        "browser.download.dir": "//home//selenium//downloads",
        "browser.download.folderList": 2,
        "browser.helperApps.neverAsk.saveToDisk": "application/octet-stream, application/x-debian-package, application/x-www-form-urlencod, application/json, application/x-compressed, application/x-zip-compressed, application/zip, multipart/x-zip, text/plain, text/csv",
        "browser.helperApps.alwaysAsk.force": false,
        "browser.download.manager.alertOnEXEOpen": false,
        "browser.download.manager.focusWhenStarting": false,
        "browser.download.useDownloadDir": true,
        "browser.download.manager.showWhenStarting": false,
        "browser.download.manager.closeWhenDone": true,
        "browser.download.manager.showAlertOnComplete": false,
        "browser.download.manager.useWindow": false,
        "browser.download.panel.shown": false
      },
      "startArguments": []
    },
    "iexplorer": {
      "webDriverVersion": "3.150.1",
      "systemArchitecture": "X64",
      "capabilities": {
        "ignoreProtectedModeSettings": true
      }
    },
    "edge": {
       "webDriverVersion": "latest"
    }
  },
  "timeouts": {
    "timeoutImplicit" : 10,
    "timeoutCondition" : 30,
    "timeoutScript" : 10,
    "timeoutPageLoad" : 15,
    "timeoutPollingInterval": 300,
    "timeoutCommand":120
  },
  "retry": {
    "number": 2,
    "pollingInterval": 11
  },
  "logger": {
    "language": "en",
    "logPageSource": true
  },
  "elementCache": {
    "isEnabled": false
  }
}
```

## Working with elements
```python
from selenium.webdriver.common.by import By
from browser.py_quality_services import PyQualityServices

browser = PyQualityServices.get_browser()

accept_btn = PyQualityServices.element_factory.get_button((By.XPATH, "//button[@id='accept-btn']"))
accept_btn.click()
```

