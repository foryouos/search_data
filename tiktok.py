import requests
import json
from lxml import etree
import re
import sys
import time
import json

if __name__=="__main__":
    url="https://aweme.snssdk.com/aweme/v1/aweme/post/?source=0&user_avatar_shrink=96_96&video_cover_shrink=248_330&publish_video_strategy_type=2&max_cursor=1596103227000&sec_user_id=MS4wLjABAAAAeIOwbcrC3X80amwtQLCCtpDO4DuiknSXSm2fxivg4xU&count=10&is_order_flow=0&os_api=22&device_type=SM-G955N&ssmix=a&manifest_version_code=130701&dpi=320&uuid=863064311681904&app_name=aweme&version_name=13.7.0&ts=1606740004&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=13709900&channel=tengxun_new&_rticket=1606740004790&device_platform=android&iid=1882004412440792&version_code=130700&cdid=a9bee84f-ef47-4108-9096-7ab40a179a4f&openudid=fa38bd6d3c116c7f&device_id=1530160689971437&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=samsung&aid=1128&mcc_mnc=46007"
    header = {
        "User-Agent": "okhttp/3.10.0.1"
    }
    cookie = {
        "Cookie": "odin_tt=bfb1b43819ba3fb692242145ea6580f6b610658dffec7974ba2df4dfa7aba85e2ccf2dcd5e36a8e298fa09ba7a4fbbf049e860bbf359bd052ea805f34ff089e6"
    }
    data = {
        "Accept-Encoding": "gzip",
        "passport-sdk-version": "18",
        "X-Tt-Token": "004dea6f13df627992012044e58b9136d7003d700576da4dcda7fd4ec7bde83de5ae458b6b0e53190ea56d00b7f6cafd8ce1c30b8f6e1c3512d7c4723f4946d8f206ce0698fe23abb303db59dfd2ec1ec7def - 1.0.0",
        "sdk-version": "2",
        "X-SS-REQ-TICKET": "1606740004792",
        "X-Khronos": "1606740004",
        "X-Gorgon": "0404e09200016bcafb662ab9cbd1c1b3d114bfd8e5b58d6fd5af",
        "Host": "aweme.snssdk.com",
        "Connection": "Keep-Alive"
    }
    page = requests.get(url=url, data=data, headers=header, cookies=cookie, timeout=100)
    page.encoding = page.apparent_encoding
    page = page.text
    print(page)