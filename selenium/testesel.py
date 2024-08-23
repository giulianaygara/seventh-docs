from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#uso do chrome webdriver
service = webdriver.ChromeService()
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com')

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf'))
)

input_element=driver.find_element(By.CLASS_NAME, 'gLFyf')
input_element.clear()
input_element.send_keys('Univali Intranet'+ Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'UNIVALI - Universidade do Vale do Itajaí - Intranet'))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, 'UNIVALI - Universidade do Vale do Itajaí - Intranet')
link.click()
time.sleep(10)
driver.quit()
