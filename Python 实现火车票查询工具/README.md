当你想查询一下火车票信息的时候，你还在上 12306 官网吗？或是打开你手机里的 APP？

下面让我们来用 Python 写一个命令行版的火车票查看器， 只要在命令行敲一行命令就能获得你想要的火车票信息！如果你刚掌握了 Python 基础，这将是个不错的小练习。

requests，使用 Python 访问 HTTP 资源的必备库。
docopt，Python3 命令行参数解析工具。
prettytable， 格式化信息打印工具，能让你像 MySQL 那样打印数据。
colorama，命令行着色工具


ps:火车有各种类型，高铁、动车、特快、快速和直达，我们希望可以提供选项只查询特定的一种或几种的火车，所以，我们应该有下面这些选项：

-g 高铁
-d 动车
-t 特快
-k 快速
-z 直达

参考地址:https://www.shiyanlou.com/courses/623/labs/2072/document