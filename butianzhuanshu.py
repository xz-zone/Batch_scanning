# coing=utf-8
import requests,json,random
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class butian(object):
    def __init__(self, page,config_info):
        self.page = page
        self.butian_url = "https://butian.360.cn/Reward/corps"
        self.data = {
            "s": 3,
            "p": self.page,
            "sort": 1,
            "token": ""
        }
        self.cookie = config_info['cookie']

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
            "Cookie":self.cookie,  # COOKIE
            "Host": "butian.360.cn",
            "Referer": "https://butian.360.cn/Reward/plan",
            "User-Agent": USER_AGENTS[random.randint(0, 2)],
            "Origin": "https://butian.360.cn",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Accept-Encoding": "gzip, deflate",
            "Content-Length": '14',
            "Connection": "keep-alive",
            "Accept-Language": "zh-CN,zh;q=0.8",
            'X-Forwarded-For': str(random.randint(1, 2)) + str(random.randint(1, 4)) + str(random.randint(1, 2)) + '.' + str(
            random.randint(1, 3)) + str(random.randint(1, 4)) + str(random.randint(1, 2)) + '.' + str(
            random.randint(1, 2)) + str(random.randint(1, 2)) + str(random.randint(1, 4)) + '.' + str(
            random.randint(1, 2)) + str(random.randint(1, 4)) + str(random.randint(1, 4)),
        }
        return self.header

    def butianjson(self):
        self.res = requests.post("https://butian.360.cn/Reward/corps", headers=self.bananer(), data=self.data)
        self.content = json.loads(self.res.content)
        result = []
        for i in range(0, len(self.content["data"]["list"]) - 1):
            result.append({'company_name':self.content["data"]["list"][i]["company_name"],'host':self.content["data"]["list"][i]["host"]})
        return result,round(self.content["data"]['count']/len(self.content["data"]["list"]))
        
    def save_txt(self, url):
        try:
            file = open("butians.txt", "a+")
            file.write("%s\n" % url)
            file.close()
        except Exception:
            pass 

class chinacycc(object):
    def __init__(self, content,config_info):
        self.content = content
        self.url = "https://d.chinacycc.com/action.php"
        # 账户
        self.username = config_info['username']
        # 密码
        self.password = config_info['password']
        # cookies
        self.cookies = "";

    # 登录
    def login(self):
        try:
            data = {
                'username':self.username,
                'password':self.password,
                'type':'login',
            }
            info = requests.post(url=self.url, data=data)
            content = json.loads(info.text)
            if content['status'] == '1':
                self.cookies = requests.utils.dict_from_cookiejar(info.cookies)
                return self.project()
            else:
                return content['msg']
        except Exception:
            pass        

    # 提交项目
    def project(self):
        try:
            data = {
                'title':self.content['company_name'],
                'domain':self.content['host'],
                'type':'add_domain',
            }
            header = {
                'Cookie':"PHPSESSID="+self.cookies['PHPSESSID'],
            }
            info = requests.post(url=self.url, data=data, headers=header)
            content = json.loads(info.text)
            if content['status'] == '1':
                return True
            else:
                return content['msg']
        except Exception:
            pass

if __name__ == "__main__":
    #子域名搜索 登录地址 https://d.chinacycc.com/index.php
    config_info = {
        'cookie':'',#补天cookice
        'username':'',#子域名搜索平台账户
        'password':'',#子域名搜索平台密码
    }
    info = butian(1,config_info)
    xxs,limit = info.butianjson()
    if limit > 1:
        for pages in range(1,limit+1):
            xxs,page = butian(pages,config_info).butianjson()
            for t in xxs:
                print(t['host'])
                info.save_txt(t['host'])
                chinacycc(t,config_info).login()
    else:
        for t in xxs:
            print(t['host'])
            info.save_txt(t['host'])
            chinacycc(t,config_info).login()