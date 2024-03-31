from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://research.danskebank.com/research/#/Research/articlelist/Danish-Mortgage-Bonds-key-figures")

driver.find_element(By.ID, "yesPro").click()

driver.find_element(By.ID, "yesEea").click()

driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div[2]/form/fieldset/a").click()
#
table = driver.find_elements(By.CLASS_NAME, "infinite-scroll-component__outerdiv")

table = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[4]")

table_2 = driver.find_elements(By.CLASS_NAME, "col-md-5 col-lg-6 col-sm-5 col-12")


anchor_elements = driver.find_elements(By.TAG_NAME, "a")

anchor_list = anchor_elements[5:]

date_list = []
for element in anchor_list:
    date_list.append(element.text.split("\n")[0])

date_list = list(filter(lambda x: x != "", date_list))


href_list = [element.get_attribute("href") for element in anchor_elements]

first_line = table[0].text.split("\n")[0]

from datetime import datetime

# Define the format of the input date string
date_format = "%d.%m.%Y"
filtered_list = [item for item in date_list if len(item) > 0 and len(item) < 10 and item != '']
date_object_list = []
# Convert the string to a datetime object
for item in filtered_list:
    date_object_list.append(datetime.strptime(item, date_format))



for date_id in date_object_list:
    formatted_date = date_id.strftime("%Y%m%d")

    url_string = f"https://research.danskebank.com/abo/SuperFlyKeyfiguresExcel{formatted_date}/$file/SuperFly_Keyfigures_Excel{formatted_date}.xlsx"

    driver.get(url_string)

# driver.find_elements(By.CLASS_NAME, "infinite-scroll-component__outerdiv")[0].click()

# driver.get("https://research.danskebank.com/abo/SuperFlyKeyfiguresExcel20231201/$file/SuperFly_Keyfigures_Excel20231201.xlsx")

import glob
import os

list_of_files = glob.glob('C:/Users/Johan/Downloads/*.xlsx') # * means all if need specific format then *.csv

xlsx_files = [file for file in list_of_files if file.endswith('.xlsx') and 'SuperFly' in file]

latest_file = max(xlsx_files, key=os.path.getctime)
import pandas as pd

df = pd.read_excel(latest_file, sheet_name="MBS", skiprows=6)