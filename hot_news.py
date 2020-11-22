import requests
import json
from lxml import etree
import re
if __name__=="__main__":
    url="http://top.baidu.com/buzz?b=1&fr=topindex"

    header={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
    }
    cookie={
     "Cookie":"BIDUPSID=8EC3D55567DBE44A8E46540D0F02D3A9; PSTM=1602818805; BAIDUID=F041DE6F44232CC1B509F1868C55AC50:FG=1; __cfduid=d7616ee597041201a1798b36feec96dab1604765549; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS=148077_152521_160918_161165_150968_160662_156286_161253_159610_148867_159875_161020_160938_160326_159383_154172_157264_160248_161419_157960_127969_161774_160101_160764_160897_161730_161442_160278_137817_161369_158982_160106_107316_158832_160801_157579_155255_159954_160423_144966_159389_159950_154212_158718_158643_155530_160981_160585_160770_160710_158504_110085; H_PS_PSSID=32819_1426_33074_33059_31253_33099_33101_32962_26350_22157; bdshare_firstime=1606008086598; delPer=0; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; PSINO=1; BA_HECTOR=21052k2l8h0kag0gr81frkd8i0r; vit=1"
    }
    data={
        "b": "1",
        "fr": "topindex"
    }
    page=requests.post(url=url,data=data,headers=header,cookies=cookie,timeout=100)
    page.encoding=page.apparent_encoding
    page=page.text
    #print(page)
    tree = etree.HTML(page)
    #获取热搜榜名称
    list_content=tree.xpath('//td[@class="keyword"]//a[@class="list-title"]//text()')
    print(list_content)

    #获得热搜榜关注数量
    list_number=tree.xpath('//td[@class="last"]//span[@class="icon-rise"]//text()')
    print(list_number)
    #获得热搜榜url

    ex='class="list-title" target="_blank" href="(.*?)" href_top='
    list_url=re.findall(ex,page)
    print(list_url)
