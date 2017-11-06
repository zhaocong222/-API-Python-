# coding: utf-8
#类来解析数据 Python通过prettytable模块将输出内容如表格方式整齐
from prettytable import PrettyTable


class TrainCollection(object):
    #空格分割
    header = '车次 车站 时间 历时 一等 二等 软卧 硬卧 硬座 无座'.split()

    def __init__(self,available_trains):
        """查询到的火车班次集合

        :param available_trains: 一个列表, 包含可获得的火车班次, 每个
                                 火车班次是一个字典
        :param options: 查询的选项, 如高铁, 动车, etc...
        """
        self.available_trains = available_trains
        #self.options = options
    
    def _get_duration(self,raw_train):
        

    def trains(self):

        for raw_train in self.available_trains:
            res = raw_train.split('|')
            if (res[1] == '预订'):
                train = [
                    res[3],  #车次
                    '-'.join([res[6],res[7]]), #车站
                    '-'.join([res[8],res[9]]), #时间
                    self._get_duration(raw_train),#历时
                                                #一等
                                                #二等
                                                #软卧
                                                #硬卧
                                                #硬座
                                                #无座
                ]
                print(res)
        
    def pretty_print(self):
        '''
        pt = PrettyTable()
        #添加头行
        pt._set_field_names(self.header)
        #增加数据
        for train in self.trains:
            pt.add_row(train)
        #打印
        print(pt)
        '''
        

