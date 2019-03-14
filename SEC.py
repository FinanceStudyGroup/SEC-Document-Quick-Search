# ----------------------------------------------------------------------------------------------------------------------
# SEC Launcher
# ----------------------------------------------------------------------------------------------------------------------

# Might not use all of these
import sys, os, re, subprocess, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ------------------------------------------------------------------------------
Ticker = raw_input("Ticker: ")
Document = raw_input("Document: ") # 10-Q  20-F  20-K  40-F  6-K
# ------------------------------------------------------------------------------

driver = webdriver.Chrome()
SEC = ("https://www.sec.gov/edgar/searchedgar/companysearch.html")
driver.get(SEC)
sleepTime=1

CIK = driver.find_element_by_css_selector('#cik')
CIK.click()
time.sleep(sleepTime)
CIK.clear()
CIK.send_keys(Ticker)

Search = driver.find_element_by_css_selector('#cik_find')
Search.click()
time.sleep(sleepTime)

DocType = driver.find_element_by_css_selector('#type')
DocType.click()
DocType.clear()
DocType = driver.find_element_by_xpath("//*[@id='type']")
DocType.send_keys(Document)
Search = driver.find_element_by_css_selector('#contentDiv > div:nth-child(2) > form > table > tbody > tr > td:nth-child(6) > input[type="submit"]:nth-child(1)')
Search.click()

# time.sleep(60)
# driver.quit()