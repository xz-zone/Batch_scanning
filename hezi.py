# coing=utf-8
import requests,json,random,time
from bs4 import BeautifulSoup

class butian(object):
    def __init__(self, page):
        self.page = page
        self.butian_url = "https://www.vulbox.com/json/getCompanyInfoByName"
        self.data = {
            "startDate": "2014-01-01",
            "endDate": "2020-01-01",
            "page": self.page,
            "search": ""
        }
        self.proxies = {"http": "113.214.13.1:8000"}
    def bananer(self):
        USER_AGENTS = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52", ]
        page = self.page
        self.header = {
            #输入你的cookie
            "Cookie":"",
            "Host": "www.vulbox.com",
            "Referer": "https://www.vulbox.com/statistics/lists",
            "User-Agent": USER_AGENTS[random.randint(0, 2)],
            "Origin": "https://www.vulbox.com",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Length": '54',
            "Connection": "keep-alive",
            "Accept-Language": "zh-CN,zh;q=0.8",
            'X-Forwarded-For': str(random.randint(1, 2))+str(random.randint(1, 4))+str(random.randint(1, 2))+'.'+str(random.randint(1, 3))+str(random.randint(1, 4))+str(random.randint(1, 2))+'.'+str(random.randint(1, 2))+str(random.randint(1, 2))+str(random.randint(1, 4))+'.'+str(random.randint(1, 2))+str(random.randint(1, 4))+str(random.randint(1, 4)),
        }
        return self.header

    def butianjson(self):
        self.res = requests.post(self.butian_url, headers=self.bananer(), data=self.data,proxies=self.proxies, timeout=10)
        self.content = json.loads(self.res.content)
        if self.content['status'] == 'success':
            result = []
            for i in range(0, len(self.content["data"]["info"]) - 1):
                url = self.content['data']['info'][i]['bus_url'].split("/")[0] + "//" + self.content['data']['info'][i]['bus_url'].split("/")[2]
                self.save_txt(url)
        else:
            exit()

    def save_txt(self, url):
        file = open("hezi.txt", "a+")
        file.write("%s\n" % url)
        file.close()



if __name__ == "__main__":
    for page in range(1,500):
        xxs = butian(page)
        xxs.butianjson()
        time.sleep(5)
