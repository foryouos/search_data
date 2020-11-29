import requests
import json
from lxml import etree
import re
import time
import json
def search(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
    }
    page = requests.get(url=url, headers=header, timeout=100)
    page.encoding = page.apparent_encoding
    page = page.text
    return page
#百度热搜的信息获取，实时信息，当天热搜，本周热搜
def baidutimehot(url):
    now_url = "http://top.baidu.com/buzz?b=1&fr=topindex"
    today_url="http://top.baidu.com/buzz?b=341&c=513&fr=topcategory_c513"
    week_url="http://top.baidu.com/buzz?b=42&c=513&fr=topbuzz_b341_c513"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
    }
    cookie = {
        "Cookie": "BIDUPSID=8EC3D55567DBE44A8E46540D0F02D3A9; PSTM=1602818805; BAIDUID=F041DE6F44232CC1B509F1868C55AC50:FG=1; __cfduid=d7616ee597041201a1798b36feec96dab1604765549; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS=148077_152521_160918_161165_150968_160662_156286_161253_159610_148867_159875_161020_160938_160326_159383_154172_157264_160248_161419_157960_127969_161774_160101_160764_160897_161730_161442_160278_137817_161369_158982_160106_107316_158832_160801_157579_155255_159954_160423_144966_159389_159950_154212_158718_158643_155530_160981_160585_160770_160710_158504_110085; H_PS_PSSID=32819_1426_33074_33059_31253_33099_33101_32962_26350_22157; bdshare_firstime=1606008086598; delPer=0; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; PSINO=1; BA_HECTOR=21052k2l8h0kag0gr81frkd8i0r; vit=1"
    }
    data = {
        "b": "1",
        "fr": "topindex"
    }
    page = requests.get(url=url, data=data, headers=header, cookies=cookie, timeout=100)
    page.encoding = page.apparent_encoding
    page = page.text
    # print(page)
    tree = etree.HTML(page)
    try:
        # 获取热搜榜名称
        list_content = tree.xpath('//td[@class="keyword"]//a[@class="list-title"]//text()')
        print(list_content)
        # time.sleep(2)
        # 获得热搜榜关注数量
        list_number = tree.xpath('//td[@class="last"]//span//text()')
        print(list_number)
        # 输出url
        ex = 'class="list-title" target="_blank" href="(.*?)" href_top='
        list_url = re.findall(ex, page)
        print(list_url)
    except:
        print("获得百度热搜出现错误，请检查百度热搜检索函数")
def weibohot():
    url="https://s.weibo.com/top/summary"
    page=search(url)
    #print(page)
    tree = etree.HTML(page)
    try:
        #获得热搜文件
        list_content=tree.xpath("//tbody//tr//td[2]//a//text()")
        #由于第一个为置顶内容，所以对列表的第一个数据进行删除：
        del list_content[0]
        #获得热度
        list_number=tree.xpath("//tbody//tr//td[2]//span//text()")
        #print(list_content)
        #print(list_number)
        dic=dict(zip(list_content,list_number))
        print(dic)
        ex = '<a href="(.*?)" target="_blank">'
        list_url =re.findall(ex, page)
        #print(list_url)
        weibo_hoturl=[]
        #循环检索数据
        for i in range(0,50):
            hot_url='https://s.weibo.com'+list_url[i]
            weibo_hoturl.append(hot_url)
        print(weibo_hoturl)
        #print(len(weibo_hoturl))

    except:
        print("微博查询出现错误，请检查微博的检索函数")
# 知乎热搜函数
def zhihuhot():
    url = "https://www.zhihu.com/hot"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
    }
    cookie ={
        "cookie" : '_zap=82c61efe-ae88-4dce-94ea-0986d83a43fc; d_c0="ADCZDssODBKPToMRarg-rfhcaeuvZ2Cur0c=|1602826829"; _xsrf=Sdn2x6R3IvqSgq9tpiwtg7koNMQ6WtwZ; q_c1=e374d817a37949bda35f684c72825a28|1603789423000|1603789423000; SESSIONID=p2HLcQqPOQr5zzRzWa39jjbTY8p5RQ8DSb3ReUR63Bf; JOID=UF8TAEq9I20miv4SJbx1e7Nc8RgzyBAgaOqqYnDxdx4W8odFXm5JqXiM-hYii15GayKxTmApUpuYj0aubwwcNOA=; osd=UFwUC0i9IGotiP4RIrd3e7Bb-hozyxcrauqpZXvzdx0R-YVFXWlCq3iP_R0gi11BYCCxTWciUJubiE2sbw8bP-I=; capsion_ticket="2|1:0|10:1606643606|14:capsion_ticket|44:ZThhMjFlMDNkMmMzNGNjNTgyNmViYjAyYmRiNzE5MjA=|f7a586e5647514122d62812cbf3aba82187b041e4def512909b961a872445342"; z_c0="2|1:0|10:1606643629|4:z_c0|92:Mi4xUHhLSkF3QUFBQUFBTUprT3l3NE1FaWNBQUFDRUFsVk5yZnpxWHdESV9MZlVPZkZwNmM2YVRrSkZtMllTOEt1Zjh3|cc94526c08564f724799a6841cb8078f9e1cef07f3bb71ed12657227b26158fa"; tst=h; tshl=; KLBRSID=fe0fceb358d671fa6cc33898c8c48b48|1606643855|1606640152'
    }

    page = requests.get(url=url, headers=header, cookies=cookie, timeout=100)
    page.encoding = page.apparent_encoding
    page = page.text
    #print(page)
    tree = etree.HTML(page)
    try:
        # 获得热搜文件
        list_content = tree.xpath('//div[@class="HotList-list"]//section//div[2]//h2//text()')
        #获取热度
        number=tree.xpath('//div[@class="HotList-list"]//section//div[2]//div//text()')
        list_number=[]
        for i in range(0,150,3):
            list_number.append(number[i])
        #获取URL
        ex = '<div class="HotItem-content"><a href="(.*?)" title="'
        list_url = re.findall(ex, page)
        #数据输出
        print(list_content)
        print(list_number)
        print(list_url)

    except:
        print("知乎热搜查询错误，请检查热搜的检索函数")
#抖音排行榜数据
def tiktok():
    url="https://www.iesdouyin.com/web/api/v2/hotsearch/billboard/word/"
    page=search(url)
    detail = json.loads(page)
    content=detail["word_list"]
    #print(content)
    list_content=[]
    list_number=[]
    for i in content:
        list_content.append(i["word"])
        list_number.append(i["hot_value"])
    #print(list_content)
    #print(list_number)
    detail=dict(zip(list_content,list_number))
    print(detail)
#检索主函数
if __name__=="__main__":

    now_url = "http://top.baidu.com/buzz?b=1&fr=topindex"
    today_url="http://top.baidu.com/buzz?b=341&c=513&fr=topcategory_c513"
    week_url="http://top.baidu.com/buzz?b=42&c=513&fr=topbuzz_b341_c513"
    #百度热搜
    print("------百度实时热搜--------")
    baidutimehot(now_url)
    print("------百度今日热搜--------")
    baidutimehot(today_url)
    print("------百度本周热搜--------")
    baidutimehot(week_url)
    #新浪微博热搜
    print("------新浪微博热搜--------")
    weibohot()
    #知乎热搜
    print("------知乎实时热搜--------")
    zhihuhot()
    print("-------抖音实时榜单--------")
    tiktok()



