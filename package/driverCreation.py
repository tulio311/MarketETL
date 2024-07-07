import joblib
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#options = Options()
#options.add_argument('--headless=new')

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    #options=options
)

time.sleep(30)

joblib.dump(driver,'headDriver.joblib')