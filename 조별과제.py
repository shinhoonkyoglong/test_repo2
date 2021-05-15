import time
import selenium
from selenium import webdriver
import matplotlib.pyplot as plt

URL = 'https://www.atfis.or.kr/sales/M002020000/search.do?salesTopItem=CD00000549&searchItem=CD00000573&searchDivision=CD00000600&searchYear=&searchQuarter=&x=61&y=35'
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path='./chromedriver.exe')#, options=options)
driver.get(url=URL)

ramyeon_list=['신라면', '진라면', '너구리', '육개장']

for i in range(4):
    search_box=driver.find_element_by_class_name("chk_list")
    search_btn.click("searchQuarter"+i)

    search_btn=driver.find_element_by_class_name("db_food_price_btns")
    search_btn.click("검색")

    ramyeon_table=driver.find_elements_by_class_name("table_view2")
    ramyeon_table_tbody=ramyeon_table[0].find_elements_by_tag_name("tbody")
    ramyeon_table_tbody_tr_list = ramyeon_table_tbody[0].find_elements_by_tag_name("tr")

    ramyeon_box = list(ramyeon_table_tbody_tr_list)
    count = 0
    for ramyeon in ramyeon_list:
        good = ramyeon_box.index(ramyeon)
        money = (ramyeon_box[good + 1])
        print(ramyeon, '=', money)
        count = count + 1
        x = count
        y = money
        plt.bar(x, y)
        plt.xticks(x, ramyeon_list, rotation='horizontal')
        plt.ylabel('단위=백만원')
        plt.subtitle(i, '분기 각 라면 매출')

    time.sleep(3)


driver.close()
