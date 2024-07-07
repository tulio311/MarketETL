from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
import joblib
import re

import xml.dom.minidom


#PATH = "C:\\Users\\Admin\\Documents\\chromedriver-win64\\chromedriver.exe"#/chromedriver.exe'
#PATH = "chromedriver.exe"

import sys

options = Options()
#options.add_argument('--headless=new')

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

#driver = joblib.load('headDriver.joblib')

# initialize a web driver instance to control a Chrome window
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.set_window_size(1920, 1080)

# scraping logic...

# if there are no CLI parameters
if len(sys.argv) <= 1:
    print('Ticker symbol CLI argument missing!')
    sys.exit(2)

# read the ticker from the CLI argument
ticker_symbol = sys.argv[1]



# stock price scraping logic omitted for brevity...
url2 = f'https://finance.yahoo.com/quote/{ticker_symbol}/key-statistics'

#driver.get(url2)
driver.get('https://finance.yahoo.com/quote/TSLA/key-statistics')


main = driver.find_element(By.ID,'Col1-0-KeyStatistics-Proxy')

datos = driver.find_elements(By.CSS_SELECTOR,'#Col1-0-KeyStatistics-Proxy > .Bxz(bb)')
print(datos[0].text)


"""
datos = main.find_elements(By.TAG_NAME,'tr')

for dato in datos:
    #value = dato.find_element(By.CLASS_NAME,'Fw(500)')
    a = dato.find_elements(By.TAG_NAME,'td')
    print(a[1].text)

    #print(dato.find_element(By.CLASS_NAME,'Fw(500) Ta(end) Pstart(10px) Miw(60px)').text)

"""



#dom = xml.dom.minidom.parse(driver.page_source) # or xml.dom.minidom.parseString(xml_string)
#pretty_xml_as_string = dom.toprettyxml()

#print(pretty_xml_as_string)

try:
    f = open("scrape.txt", "w")
    f.write("Escrito")   
    f.close()
except IOError as errno:
    print(errno)



#forward_pe = driver.find_element(By.CSS_SELECTOR, '.Fw(500)').text

#print(type(driver.page_source))











# close the browser and free up the resources
driver.quit()

