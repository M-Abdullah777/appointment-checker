import logging
import time
from bs4 import BeautifulSoup
from seleniumbase import Driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def check():
    driver = webdriver.Chrome() 

    try:
        url = "https://service2.diplo.de/rktermin/extern/choose_categoryList.do?locationCode=isla&realmId=108"
        driver.get(url)
        current_html = driver.page_source

        # Check for new appointment waiting lists
        soup = BeautifulSoup(current_html, 'html.parser')
        appointment_lists = soup.find_all('div', style='font-size: 14pt; font-weight: bold; margin-bottom: 1em;')
        for appointment_list in appointment_lists:
            appointment_text = appointment_list.get_text(strip=True)
          
            if 'study visa' in appointment_text:
                print("Change Detected: New appointment waiting list for Study visa found.")
                # Perform any action you want here
                active = True
                return (None, True)
                

            else:
                active = False
                print("No Change Detected")

        if active:
            print('ACTIVE')
            driver.quit()
            return (None, True)
            # print(active_value)
        else:
            print('NOT-ACTIVE')
            driver.quit()
            return (None, False)
              

    except Exception as e:
        print('ERROR')
        logging.error('An error occurred: %s', e)
        # Handle error as needed
        return (e, False)
        

    finally:
        driver.quit()

if __name__ == '__main__':
    while True:
        error, result = check()
        if error:
            print(f"An error occurred: {error}")
        if result:
            print('ACTIVE')
        else:
            print('NOT-ACTIVE')