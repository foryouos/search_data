import requests
import json
import time

print("调用魔声检索音乐数据,目前仅咪咕平台(mg)，网易云音乐MV，没有问题")
#content=input("输入需要下载的平台")
songs=input("请输入你要搜索的歌曲")
content="mg"
#songs="那些年"
url="http://music.moresound.tk/api.php?search="+content
download_url="http://music.moresound.tk/api.php?get_song="+content
#print(url)
header={
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Content-Length":"38",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
    "Host": "music.moresound.tk",
    "Origin": "http://music.moresound.tk",
}
header_download={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "music.moresound.tk",
    "Upgrade-Insecure-Requests": "1"
}
cookie_download={
    "Cookie": "XLA_CI=dcbb683de7339ca50e098227249b7551; IP=FCOBeqRjtxBeGRJaDhZdADeR9wFSmL0KiJNZs8ui2NA%253D; QQMUSIC_SIP=%5B%22http%3A//119.167.131.31/amobile.music.tc.qq.com/%22%2C%22http%3A//119.167.131.32/amobile.music.tc.qq.com/%22%2C%22http%3A//119.167.131.33/amobile.music.tc.qq.com/%22%5D; QQ="
}
cookie={
    "Cookie": "XLA_CI=dcbb683de7339ca50e098227249b7551; IP=FCOBeqRjtxBeGRJaDhZdADeR9wFSmL0KiJNZs8ui2NA%253D; QQMUSIC_SIP=%5B%22http%3A//119.167.131.27/amobile.music.tc.qq.com/%22%2C%22http%3A//119.167.131.28/amobile.music.tc.qq.com/%22%2C%22http%3A//119.167.131.29/amobile.music.tc.qq.com/%22%5D; QQ="
}
data={
    "w": songs,
    "p": "1",
    "n": "20"
}
#print(data)
page=requests.post(url=url,data=data,headers=header,cookies=cookie,timeout=100)
page.encoding=page.apparent_encoding
detail=page.text
detail=(detail)
#将字符串转为字典
detail = json.loads(detail)
#对特定数据进行输出
#print(type(detail)) #检测输出类型
#print(len(detail)) #检测输出长度
#print(detail)
song_list =detail["song_list"]
#print(song_list)
for song in song_list:
    # 获取进行音乐下载的songmid 代码
    songid=song["songmid"]
    download_data={
        "mid":songid
    }
    #print(download_data)
    #print(download_url)
    time.sleep(1)
    download_detail = requests.post(url=download_url, data=download_data, headers=header, cookies=cookie, timeout=10)
    download_detail.encoding = download_detail.apparent_encoding
    download_detail = download_detail.text
    # 判断类型进行修改
    # print(type(download_detail))
    download_detail = json.loads(download_detail)
    time.sleep(1)
    # 获取歌曲信息
    try:
        singer = download_detail["singer"] + download_detail["song"]
        print(singer)
        #获得下载信息
        downfile=download_detail["url"]
        #print(downfile)
        for i in downfile:
            print(i)
            #print(downfile[i])
            if downfile[i]!=str(None):
                downfile_url = "http://music.moresound.tk/" + str(downfile[i])
                #print(downfile_url)
                time.sleep(2)
                #进行分成加成url下载链接数据
                download = requests.get(url=downfile_url, headers=header_download, cookies=cookie_download, timeout=100)
                download.encoding = download.apparent_encoding
                download = download.text
                # 转化为字典
                try:
                    downloadjson = json.loads(download)
                    download_last = downloadjson["url"]
                    print(download_last)
                except :
                    continue
    except:
        continue





