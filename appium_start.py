from appium import webdriver
from selenium.webdriver.common.by import By
import time

executor = 'http://127.0.0.1:4723/wd/hub'

desired_capabilities = {
    "platformName": "Android",
    "appPackage": "ru.utkonos.android.utkonoid",
    "deviceName": "R58NB0NN79X",
    "appActivity": "ru.utkonos.for_customers.online_store.presentation.activity.splash_screen.SplashScreenActivity"
}


driver = webdriver.Remote(command_executor=executor,
                          desired_capabilities=desired_capabilities)


time.sleep(15)
main_button = driver.find_element(By.ID, "ru.utkonos.android.utkonoid:id/action_main")
print(f'нашел баттон {main_button}')
time.sleep(14)

main_button.click()
print(f'нажал баттон {main_button}')
time.sleep(15).
