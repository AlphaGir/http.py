# http.py
用于批量扫描功能。<strong>功能点没有什么新意</strong>，主要是个人学习python编程和个人使用。有些大型项目里可能用得到，小项目没有什么用。。。哈哈哈哈
这些功能一些扫描器其实都有。甚至比较完备。但是呢不想安装，然后锻炼一下python编程能力，实际上我以前从来没有写过python代码，以后需要Python地方还很多。

环境:python3 urllib bs4  BeautifulSoup

* 1.从文件批量扫描url 判断url访问 python3 http.py -url url文件目录
* 2.ip反查域名，以及对应域名访问情况 python3 http.py -ip:domain ip文件目录

后期会增加 子域名 端口扫描功能或者其他我个人需要的功能。<strong>以我个人项目实际需求为主。</strong>

目前存在bug：
        * 域名访问，很多域名可能是https://www去访问,http：直接访问。还有无法访问抛出异常情况。虽然做了异常定义。
        * Ip反查域名是根据两个在线网站爬取，在线网站容易挂，或者超时。
        * 还有因为代码问题已经网络访问问题 运行起来太慢了。
