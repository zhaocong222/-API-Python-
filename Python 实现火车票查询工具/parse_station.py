import re
import requests
from pprint import pprint

'''
命令行操作:  python3 ./parse_station.py  > stations.py 生成到文件

使用 pprint 模块
pprint 模块( pretty printer )
用于打印 Python 数据结构. 当你在命令行下打印特定数据结构时你会发现它很有用(输出格式比较整齐, 便于阅读).
'''

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9030'
#verify 设置为 False，Requests 也能忽略对 SSL 证书的验证。
res = requests.get(url,verify=False)
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',res.text)

#格式化为字典ls
pprint(dict(stations), indent=4)
