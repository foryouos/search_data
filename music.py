import requests
import json
if __name__ =="__main__":

    #音乐请求端口 此端口为post请求
    url="https://app.onenine.cc/m/api/search"
    header={
        "authority": "app.onenine.cc",
        "method": "POST",
        "path": "/m/api/search",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding":"gzip,deflate,br",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-length": "88",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    #data数据与名称到底有什么联系，而且每一次还不一样，关键上次的还可以搜索，这是什么愿意呢？？？
    data={
        #就是这个data决定着音乐的选择
        "data": "de2buhd-hjBu5JevuF026iVIgsusf1g1fo5GHPNrhVwdGJKnzqDxYehsEvlz-wB_deVqPAxnhfsXFdIO",
        "v": "2"
    }
    r=requests.post(url=url,data=data,headers=header)
    r.encoding=r.apparent_encoding
    r=r.text
    #转为json格式
    detail = json.loads(r)
    #print(detail)
    #转为data的json目录下
    data=detail["data"]
    #转到音乐list的音乐目录下
    list=data["list"]
    for li in list:
        print(li)

