# coding: utf-8

"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""
from docopt import docopt
from stations import stations
import requests
#去掉警告 InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.org/en/latest/security.html  InsecureRequestWarning)
from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
from TrainsCollection import TrainCollection


#docopt 会根据我们在 docstring 中的定义的格式自动解析出参数并返回一个字典，也就是 arguments
def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
    #print(arguments)
    train_date = arguments['<date>']
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])

    #构建url
    url = ('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT').format(
        train_date,from_station,to_station    
    )
    return url

#显示火车票
def show():
    # 添加verify=False参数不验证证书
    url = cli()
    r = requests.get(url, verify=False)
    available_trains = r.json()['data']['result']
    city    = r.json()['data']['map']
    #解析数据并显示
    TrainCollection(available_trains,city).pretty_print()

if __name__ == '__main__':
    show()


