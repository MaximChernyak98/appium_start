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


https: // download.oracle.com/otn-pub/java/jdk/8u281-b09/89d678f2be164786b292527658ca1605/jre-8u281-windows-x64.exe
