import requests
import os
import json
from bs4 import BeautifulSoup

domain="https://8018ow.top"
update="https://github.com/8xx8x/8x8x"

def get_data(page):
    if page==1:
        return requests.get(domain+"/video").text
    else:
        return requests.get(domain+"/video/page/%s/"%page).text

def analysis_page(html):
    soup=BeautifulSoup(open("temp.html"),features="html5lib")
    for page in soup.find_all("a"):
        print(page)
        if "末页" in page:
            last_page=BeautifulSoup(str(page),features="html5lib").a["href"].split("/")[-2]
    ul=soup.find_all("li")
    new_ul=[]
    for u in ul:
        if "<a href=\"/video/" in str(u):
            new_ul.append(BeautifulSoup(str(u),features="html5lib").p)
    data=[]
    for ll in new_ul[1:-1]:
        new_ll=BeautifulSoup(str(ll),features="html5lib")
        data.append({'name':"".join(new_ll.p.string.split("-")[:-1]),'url':domain+new_ll.a["href"],'tag':new_ll.p.string.split("-")[-1]})
    return data,last_page

def analysis_video(href):
    soup=BeautifulSoup(requests.get(domain+"/video/%s/"%href).text,features="html5lib")
    for h in soup.find_all("h1"):
        if "lhgt" in str(h):
            aname=BeautifulSoup(str(h),features="html5lib").h1.string
    for li in soup.find_all("li"):
        if ".mp4" in str(li):
            url=BeautifulSoup(str(li),features="html5lib").a["href"]
    return {'name':"".join(aname.split("-")[:-1]),'url':domain+'/video/%s'%href,'id':href,'dl':url,'tag':aname.split("-")[-1]}

def search(word,page):
    r=requests.post('https://s.%s/search'%domain.replace('https://',''),headers={'Content-type':'application/x-www-form-urlencoded'},data={'title':str(word),'current':str(page),'size':'16','source':'v1'})
    data=json.loads(r.text)
    return data['data'],data['totalPage'],data['page']

def star(href):
    da=analysis_video(href)
    with open("data.json","r")as data:
        data=json.loads(data.read())
        data.append(da)
    with open("data.json","w")as new_data:
        new_data.write(json.dumps(data,ensure_ascii=False))

def show_star():
    with open("data.json","r")as data:
        for d in json.loads(data.read()):
            print("\033[1;33m%s\033[0m\n├── 链接: \033[1;35m%s\033[0m\n├── 下载: \033[1;32m%s\033[0m\n├── 标签: \033[1;31m%s\033[0m\n└── ID: \033[1;36m%s\033[0m\n"%(d["name"],d["url"],d["dl"],d["tag"],d["id"]))

dashboard=["浏览页面","获取视频",'搜索',"收藏视频","展示收藏"]
for dash in dashboard:
    print(str(dashboard.index(dash))+". "+dash)
mode=int(input("请输入序号以继续:"))
if mode==0:
    pid=int(input("请输入页面序号:"))
    data=get_data(pid)
    with open("temp.html","w")as f:
        f.write(data)
    data,last_page=analysis_page(data)
    os.system("clear")
    print("当前页面: %s - 共有页面: %s\n"%(pid,last_page))
    for d in data:
        print("\033[1;33m%s\033[0m\n├── 链接: \033[1;35m%s\033[0m\n├── 标签: \033[1;31m%s\033[0m\n└── ID: \033[1;36m%s\033[0m\n"%(d['name'],d['url'],d['tag'],d['url'].split("/")[-2]))
if mode==1:
    data=analysis_video(input("请输入视频ID:"))
    os.system("clear")
    print("\033[1;33m%s\033[0m\n├── 链接: \033[1;35m%s\033[0m\n└── 标签: \033[1;31m%s\033[0m\n"%(data['name'],data['dl'],data['tag']))                                  
if mode==2:
    data,last_page,now_page=search(input('请输入关键词:'),input('请输入搜索页码(不确定请输入1):'))
    os.system("clear")
    print("当前页面: %s - 共有页面: %s\n"%(now_page,last_page))
    for d in data:
        print('\033[1;33m%s\033[0m\n├── 链接: \033[1;35m%s\033[0m\n├── 标签: \033[1;31m%s\033[0m\n└── ID: \033[1;36m%s\033[0m\n'%(''.join(d['videoTitle'].split('-')[:-1]),domain+d['pageUrl'],d['videoTitle'].split('-')[-1],d['videoInfoId']))
if mode==3:
    star(input("请输入视频ID:"))
if mode==4:
    show_star()
else:
    print("Bye")