from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_car_washing():
    browser = webdriver.Chrome()
    browser.get('https://car-washing-eng.herokuapp.com/')

    browser.find_element(By.NAME, 'brand').send_keys('KIA RIO')
    browser.find_element(By.NAME, 'number').send_keys('Y567YU 78')
    browser.find_element(By.NAME, 'phone').send_keys('+7-901-212-85-06')
    browser.find_element(By.NAME, 'name').send_keys('Kate Smith')
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    assert WebDriverWait(browser, 100).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="__next"]/div/div/p'), 'Request sent!')) == True

    browser.quit()
