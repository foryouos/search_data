import requests
import json
from lxml import etree
import re
import sys
import time
import json

if __name__=="__main__":
    #借用其它网站的解析端口,由于本人能力有限，因此在此使用的解析路径为第三方网站的
    #tiktok_url=input("请输出你要下载原图的抖音URL")
    movie_url=input("请输入抖音视频URL")
    url="https://api.cooluc.com/?url="+str(movie_url)
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    page = requests.post(url=url, headers=header, timeout=100)
    page.encoding = page.apparent_encoding
    page = page.text
    a=str(page[0:5:1])   # 删除对于的<pre>
    detail=page.replace(a,"")
    try:
        detail=json.loads(detail)
        #print(detail)
        if detail["success"]==True:
            #print(type(detail))
            print("抖音号信息："+detail["nickname"])
            print("短视频相关描述信息："+detail["desc"])
            print("无水印下载链接："+detail["url"])
        else:
            print("请检查URL是否出现错误,解析出现报错")
    except:
        print("请使用抖音的短链接，url前不要出现空格，很可能出现链接错误")