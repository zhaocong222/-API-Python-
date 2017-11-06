# coding: utf-8
#类来解析数据 Python通过prettytable模块将输出内容如表格方式整齐
from prettytable import PrettyTable


class TrainCollection(object):
    #空格分割
    header = '车次 车站 时间 历时'.split()

    def __init__(self,available_trains,city):
        """查询到的火车班次集合

        :param available_trains: 一个列表, 包含可获得的火车班次, 每个
                                 火车班次是一个字典
        :param options: 查询的选项, 如高铁, 动车, etc...
        """
        self.available_trains = available_trains
        self.city = city
    
    def _get_duration(self,duration):
        
        duration = duration.replace(':','小时') + '分'
        if duration.startswith('00'):
            return duration[4:] #只有分就从第4个位置开始截取
        if duration.startswith('0'):
            return duration[1:] #从第1个位置开始截取
        return duration
        
    # @property 配合 yield高级用法
    @property
    def trains(self):

        for raw_train in self.available_trains:
            
            res = raw_train.split('|')
            train = [
                res[3],  #车次
                '-'.join([self.city.get(res[6]),self.city.get(res[7])]), #车站
                '-'.join([res[8],res[9]]), #时间
                self._get_duration(res[10]),#历时
            ]
            
            yield train

    def pretty_print(self):

        pt = PrettyTable(self.header)
        #增加数据
        for train in self.trains:
        #pt.add_row(['g123','武汉-长沙','xxx','xxx'])
            pt.add_row(train)
        #打印
        print(pt)
        

