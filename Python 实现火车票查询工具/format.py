# coding: utf-8
#format 用法测试

date = '2017-10-10'
from_sta = '武汉'
to_sta = '长沙'

str = '出发地:{},目的地:{},到达实践:{}'.format(
    from_sta,to_sta,date
)

print(str)