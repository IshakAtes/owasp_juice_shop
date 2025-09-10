from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

url = "http://127.0.0.1:3000/#"
driver_path = "/usr/local/bin/geckodriver"

options = Options()
options.add_argument("--headless")  # optional: ohne Browser-Fenster

service = Service(executable_path=driver_path)
driver = webdriver.Firefox(service=service, options=options)

driver.get(url)

page_source = driver.page_source
print(page_source)

driver.quit()
