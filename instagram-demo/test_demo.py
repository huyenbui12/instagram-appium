from appium import webdriver
from selenium.webdriver.common.by import By
import unittest

desire_capabilities = {
  "platformName": "Android",
  "platformVersion": "12",
  "deviceName": "emulator-5554",
  "automationName": "appium",
  "app": "/Users/huyenbui/Downloads/instagram.apk",
  "appWaitActivity": "*"
}

driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desire_capabilities)

class Test(unittest.TestCase):
  
  def test_click_create(self):
    # click create account button
    create_account_btn = driver.find_element(By.ID, 'com.instagram.android:id/sign_up_with_email_or_phone')
    create_account_btn.click()
    # wait for 2s
    driver.implicitly_wait(2)
    # verify
    email_tab = driver.find_element(By.ID, 'com.instagram.android:id/right_tab')
    assert email_tab.is_displayed()

  def test_switch_email(self):
    # click email tab
    email_tab = driver.find_element(By.ID, 'com.instagram.android:id/right_tab')
    email_tab.click()
    # wait for 2s
    driver.implicitly_wait(2)
    # verify
    email_field = driver.find_element(By.ID, 'com.instagram.android:id/email_field')
    assert email_field.is_displayed()

  def test_enter_email(self):
    email_tab = driver.find_element(By.ID, 'com.instagram.android:id/right_tab')
    email_tab.click()
    email_field = driver.find_element(By.ID, 'com.instagram.android:id/email_field')
    email_field.send_keys('thaohuyen@gmail.com')
    email_clear_btn = driver.find_element(By.ID, 'com.instagram.android:id/email_clear_button')
    assert email_clear_btn.is_displayed()

if __name__ == '__main__':
    unittest.main()
