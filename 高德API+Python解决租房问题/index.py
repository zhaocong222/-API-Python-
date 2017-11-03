#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import csv

#爬取的链接地址
url = "http://wh.58.com/pinpaigongyu/pn/{page}/?minprice=600_5000"

page = 0

csv_file = open("./rent.csv","w")
csv_writer = csv.writer(csv_file)

while True:
    
    page += 1
    print("fetch:",url.format(page=page))
    res = requests.get(url.format(page=page))
    html = BeautifulSoup(res.text,'lxml')

    house_list = html.select(".list > li")

    #循环在读不到新的房源时结束
    if not house_list:
        break

    for house in house_list:
        #house.select("h2")[0] 不是字符串类型
        house_title = house.select("h2")[0].string
        house_url = urljoin(url,house.select("a")[0]["href"])
        house_info_list = house_title.split()

        # 如果第二列包含公寓或者青年社区 取第一列为地址
        if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
            house_location = house_info_list[0]
        else:
            house_location = house_info_list[1]
        
        house_money = house.select(".money")[0].select("b")[0].string
        
        #写入csv
        csv_writer.writerow([house_title,house_location,house_money,house_url])
 
csv_file.close()




