import urllib
import random
import sys
import urllib.request
from urllib import error, request
from bs4 import BeautifulSoup
'''
主要功能：从文件里按行读取url/ip 获取响应码 判断url能不能访问
         查询ip对应域名
 
环境：python3
使用 python3 http.py -url 文件
     python3 http.py -ip:domain 文件
     python3 http.py -ip 文件
'''

def u(strlist):
    req=request.Request(strlist)
    try:
        response = request.urlopen(req,timeout=0.8)
       # html = response.read().decode('utf-8')
        print(str(response.status)+":"+strlist)
    except error.URLError as e:
        if hasattr(e, 'code'):
            print("HTTPError")
            print(e.code)
        elif hasattr(e, 'reason'):
            print("URLError")
            print(e.reason)
def url(strl):
    req = request.Request("http://"+strl)
    try:
        response = request.urlopen(req,timeout=0.9)
       # html = response.read().decode('utf-8')
        print(response.status)
    except error.URLError as e:
        if hasattr(e, 'code'):
            print("HTTPError")
            print(e.code)
        elif hasattr(e, 'reason'):
            print("URLError")
            print(e.reason)

def dnsurl(strs,a):
    homeReq = urllib.request.Request(
    #url = "https://site.ip138.com/110.75.129.5/"
    url = "https://www.dnsgrep.cn/ip/"+strs)

    #homeReq.add_header('Host', 'site.ip138.com');
    homeReq.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0');
    #homeReq.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8');
    #homeReq.add_header('Accept-Language', 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2')
    a=random.randint(1,255)
    b=random.randint(1,255)
    c=random.randint(1,255)
    d=random.randint(1,255)

    s=str(a)+"."+str(b)+"."+str(c)+"."+str(d)
   
    homeReq.add_header('x-forwarded-for', s)
    #homeReq.add_header('Cookie', 'Hm_lvt_134bc9f365ea67c4ed9a404f48e827e4=1652594692; Hm_lpvt_134bc9f365ea67c4ed9a404f48e827e4=1652594692');
    #homeReq.add_header('Connection', 'Keep-Alive');
    resp = urllib.request.urlopen(homeReq).read().decode('utf-8')
    soup = BeautifulSoup(resp, "html.parser")
    #print(soup.li)
    all_a = soup.find('div', id='result').find_all('td')
    for a in all_a:
        title = a.get_text()  # 提取文本
        #print("标题：" + title)
        t = title
        if t.count('.com') > 0 or t.count(".cn")>0:
           print("标题1：" + title)
           if a==1:
              url(title)
           else:
               print("-------------------------------------------------------")
 
'''
all_a = soup.find('ul', id='list').find_all('a', target='_blank')
for a in all_a:
    title = a.get_text()  # 提取文本
    if(title != ''):
      print("标题：" + title)
'''



def main():
    if sys.argv[1]=='-ip':
        f= open(sys.argv[2])
        for line in f:
          dnsurl(line,1)
        f.close()
    elif sys.argv[1]=='-url':
        f = open(sys.argv[2])
        for line in f:
            u(line)
        f.close()
    elif sys.argv[1]=='-ip:domain':
        f = open(sys.argv[2])
        for line in f:
            dnsurl(line,0)
        f.close()
    else:
        print("incoding……")
        
if __name__ == "__main__":
    main()
