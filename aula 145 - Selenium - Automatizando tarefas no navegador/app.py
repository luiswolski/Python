from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'chromedriver.exe '


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=CHROME_DRIVER_PATH,
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser



if __name__ == '__main__':
    options = ('--disable-gpu', '--no-sandbox',)
    browser = make_chrome_browser(*options)

    browser.get('https://github.com/')
   # sleep(2)

    browser.maximize_window()

    #sleep(2)
    try:
        btn_sign_in = browser.find_element(By.LINK_TEXT, 'Sign in')
        btn_sign_in.click()
    except Exception as e:
        print('Erro ao clicar em Sign in:', e)

    sleep(1)
    try:
        input_login = browser.find_element(By.ID, 'login_field')
        input_login.send_keys('EMAIL_DO_USUARIO')
        input_password = browser.find_element(By.ID, 'password')
        input_password.send_keys('SENHA_DO_USUARIO')
        btn_login = browser.find_element(By.NAME, 'commit')
        btn_login.click()
    except Exception as e:
        print('Erro ao inserir senha:', e)

    sleep(1)
    try:
        btn_perfil = browser.find_element(By.CSS_SELECTOR, 'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary')
        btn_perfil.click()
    except Exception as e:
        print('Erro ao clicar no perfil:', e)

    sleep(1)
    verifica_user = browser.find_element(By.CLASS_NAME, 'user-profile-link')
    verifica_user_html = verifica_user.get_attribute('innerHTML')
    assert 'NOME_DE_USUARIO' in verifica_user_html



    sleep(5)
    try:
        btn_logout = browser.find_element(By.CSS_SELECTOR, 'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
        btn_logout.click()
    except Exception as e:
        print('Erro ao clicar no logout:', e)


    sleep(4)
    browser.quit()
