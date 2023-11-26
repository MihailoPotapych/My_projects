from selenium import webdriver as wd
from working_with_DB import get_user_data
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_valid_session_id():
    raw_user_data = get_user_data()
    if raw_user_data[0] == (None, None):
        return False
    auth = {'login': raw_user_data[0][0], 'password': raw_user_data[0][1]}
    url = 'https://sh-open.ris61edu.ru/auth/login-page'
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--headless')
    print('Подождите, пожалуйста. Это не должно занять много времени.')
    driver = wd.Chrome(options=options)
    print('Почти готово...')
    driver.get(url)

    login_id = 'username'
    password_id = 'password'
    button_id = 'form-submit'

    login_entry = driver.find_element('id', login_id)
    password_entry = driver.find_element('id', password_id)
    send_button = driver.find_element('id', button_id)

    login_entry.send_keys(auth['login'])
    password_entry.send_keys(auth['password'])
    send_button.click()

    try:
        elem = WebDriverWait(driver, 10).until(
            EC.title_contains('БАРС'))
    except TimeoutException:
        err = driver.find_element('id', 'form-error').get_attribute('innerHTML')
        return 'error'
    
    return driver.get_cookies()[-2]['value']    
    driver.quit()