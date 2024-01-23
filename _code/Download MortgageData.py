from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
# driver.get("https://research.danskebank.com/research/#/Research/articlelist/Danish-Mortgage-Bonds-key-figures")
#
# driver.find_element(By.ID, "yesPro").click()
#
# driver.find_element(By.ID, "yesEea").click()
#
# driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div[2]/form/fieldset/a").click()
#
# table = driver.find_elements(By.CLASS_NAME, "infinite-scroll-component__outerdiv")
#
# driver.find_elements(By.CLASS_NAME, "infinite-scroll-component__outerdiv")[0].click()

# driver.get("https://research.danskebank.com/abo/SuperFlyKeyfiguresExcel20231201/$file/SuperFly_Keyfigures_Excel20231201.xlsx")

driver.get("https://research.danskebank.com/abo/SuperFlyKeyfiguresExcel20231204/$file/SuperFly_Keyfigures_Excel20231204.xlsx")

# import glob
# import os
#
# list_of_files = glob.glob('C:/Users/Johan/Downloads/*.xlsx') # * means all if need specific format then *.csv
# latest_file = max(list_of_files, key=os.path.getctime)
#
# import pandas as pd
#
# df = pd.read_excel(latest_file, sheet_name="MBS", skiprows=6)