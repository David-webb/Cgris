# -*-coding:utf-8 -*-
__author__ = 'TengWei'

import requests
import traceback
import httplib
import urllib
import json

# 从网页提取的数据(utf8编码)无法正常显示
# 设置系统内部的编码为utf8
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


class getDocsByPost():
    """
        Accept
        Accept-Encoding
        Accept-Language
        Cache-Control
        Connection
        Content-Length
        Content-Type
        Cookie
        CNZZDATA1259170489=193497948-1484573134-http%253A%252F%252Fwww.cgris.net%252F%7C1484573134; PHPSESSID
        =7b411f42f754ab32290f6b7a06ead27a
        Host
        Referer
        X-Prototype-Version
        X-Requested-With
    """
    headers = {
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "www.cgris.net",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
        "Referer": "http://www.cgris.net/query/croplist.php",
        "Origin": "http://www.cgris.net",
        "X-Prototype-Version": "1.5.1.1",
        "X-Requested-With": "XMLHttpRequest",
    }
    aurl = "http://www.cgris.net/query/o.php"  # post 使用的url


    def getAjaxData(self):
        data = {
            "action": "menu",
            # "_":""
        }
        data_encode = urllib.urlencode(data)
        print data_encode
        # res = requests.post(self.aurl, data=data_encode)
        # print res.status_code
        # with open('tmppage.txt', 'w') as wr:
        #     wr.write(res.text)

        httpClient = None
        try:
            httpClient = httplib.HTTPConnection("www.cgris.net", 80, timeout=60)
            httpClient.request(method="POST", url=self.aurl, body=data_encode, headers=self.headers)
            response = httpClient.getresponse()
            tmppage = json.loads(response.read())
            # with open('menu.txt', 'w') as wr:
            #     wr.write(json.dumps(tmppage))
            # jsonbuf = json.loads(tmppage)
            # mlist = jsonbuf["documents"]
            # totalpages = jsonbuf["pageTotal"]
            # print response.status
            # print response.reason
            # print response.version
            # print response.read()
            # print response.getheaders() # 获取头信息
        except Exception, e:
            print traceback.format_exc()
            return False
        finally:
            if httpClient:
                httpClient.close()
        # print  totalpages
        # return mlist  # len(mlist), totalpages
        return tmppage
        pass


if __name__ == '__main__':
    # tmp = getDocsByPost()
    # tmp.getAjaxData()
    # for seed in tmp.getAjaxData():
    #     print seed[0], seed[1]

    with open('menu.txt', 'r')as rd:
        # print rd.read()
        tmpmenu = json.loads(rd.readline())
    #
    for seed in tmpmenu:
        print seed[0], seed[1]

    # j = 0
    # for i in range(0, 10):
    #     print i
    #     j = i

    pass
