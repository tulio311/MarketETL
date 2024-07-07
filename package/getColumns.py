import joblib
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException

import re

options = Options()
options.add_argument('--headless=new')

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

# initialize a web driver instance to control a Chrome window
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#driver.set_window_size(1920, 1080)
stock={}

# Statistics scrapping

url2 = f'https://finance.yahoo.com/quote/TSLA/key-statistics'

driver.get(url2)

main = driver.find_element(By.ID,'Col1-0-KeyStatistics-Proxy')
datos = main.find_elements(By.TAG_NAME,'tr')

f = open('cols.txt','a')

for dato in datos:
    a = dato.find_elements(By.TAG_NAME,'td')
    key = a[0].text
    value = a[1].text

    if re.search(r"20\d\d", key):
        index = key.find('(')
        if key[index+1] == 'p':
            key = key[:index-1] + '_prior'
        else:
            key = key[:index-1]

    key = '_' + key

    replacing = {'/':'_', ' ':'_', '&':'_', '(':'_', ')':'_','-':'_', '%':'perc'}
    for rep in replacing:
        key = key.replace(rep,replacing[rep])
    if key[-1].isdigit() == True:
        key = key[:-2]


    print(key)
    f.write(key + '\n')
    stock[key] = value

f.close()

    #print(dato.find_element(By.CLASS_NAME,'Fw(500) Ta(end) Pstart(10px) Miw(60px)').text)


#forward_pe = driver.find_element(By.CSS_SELECTOR, '.Fw(500)').text

#print



# close the browser and free up the resources
driver.quit()
