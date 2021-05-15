import time
import selenium
from selenium import webdriver

URL = 'https://www.atfis.or.kr/sales/M002020000/search.do?salesTopItem=CD00000549&searchItem=CD00000573&searchDivision=CD00000600&searchYear=&searchQuarter=&x=61&y=35'
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url=URL)

for name in range(4):
    keyword_list_div = driver.find_elements_by_class_name("")
    print(len(keyword_list_div))

    date = keyword_list_div[0].find_element_by_class_name("no").text
    print("--", f"date : {date}", "--")

    prev_button = keyword_list_div[0].find_element_by_class_name("pre")

    keyword_list_div_row_list = keyword_list_div[0].find_elements_by_class_name("keywd_rank")
    print(len(keyword_list_div_row_list))
    for keyword_list_div_row in keyword_list_div_row_list:
        rank = keyword_list_div_row.find_element_by_class_name("rank").text
        keyword = keyword_list_div_row.find_element_by_class_name("keywd").text
        print("\t", rank + " - " + keyword)
    print("----")
    print("")

    prev_button.click()
    time.sleep(3)

time.sleep(3)

driver.close()
