from appium import webdriver

executor = 'http://127.0.0.1:4723/wd/hub'

desired_capabilities = {
    platformName: "Android",
    platformVersion: "8",
    deviceName: "Android Emulator",
    app: "/path/to/the/downloaded/ApiDemos-debug.apk",
}

driver = webdriver.Remote(
    command_executor=executor,
    desired_capabilities=desired_capabilities)
