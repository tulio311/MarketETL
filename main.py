from apscheduler.schedulers.blocking import BlockingScheduler
import sqlite3
import pandas as pd
from package.scraper import scrapeTicker
from package.dbWriter import writeRowTicker


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException

import logging

logging.basicConfig(filename='my_script.log', level=logging.DEBUG)

sched = BlockingScheduler()

def daily():

    # Obtain database connection and tickers
    conn = sqlite3.connect('Market.db',isolation_level=None)

    tickers = pd.read_csv('tickers.csv')
    print(tickers)

    """
    options = Options()
    options.add_argument('--headless=new')

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    """
    
    # Loop over tickers
    try:
        for i in range(len(tickers)):
            data = 0
            ticker = tickers.iloc[i,0]

            try:
                data = scrapeTicker(ticker,'a')#,driver)
                print(data)
            except Exception:
                print(f'No {ticker}')

            if data != 0:
                writeRowTicker(data, ticker, conn)


    finally:
        #driver.quit()
        conn.close()

    


daily()

#sched.add_job(daily, 'cron', hour = 16, minute = 16)
#sched.start()