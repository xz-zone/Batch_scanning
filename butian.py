# coing=utf-8
import requests,json,random
from bs4 import BeautifulSoup

class butian(object):
    def __init__(self, page):
        self.page = page
        self.butian_url = "http://loudong.360.cn/Reward/pub"
        self.data = {
            "s": 1,
            "p": self.page,
            "token": ""
        }

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
            "Host": "loudong.360.cn",
            "Referer": "http://loudong.360.cn/Service",
            "User-Agent": USER_AGENTS[random.randint(0, 2)],
            "Origin": "http://loudong.360.cn",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Accept-Encoding": "gzip, deflate",
            "Content-Length": '14',
            "Connection": "keep-alive",
            "Accept-Language": "zh-CN,zh;q=0.8",
            'X-Forwarded-For': str(random.randint(1, 2))+str(random.randint(1, 4))+str(random.randint(1, 2))+'.'+str(random.randint(1, 3))+str(random.randint(1, 4))+str(random.randint(1, 2))+'.'+str(random.randint(1, 2))+str(random.randint(1, 2))+str(random.randint(1, 4))+'.'+str(random.randint(1, 2))+str(random.randint(1, 4))+str(random.randint(1, 4)),
        }
        return self.header

    def butianjson(self):
        self.res = requests.post("http://loudong.360.cn/Reward/pub", headers=self.bananer(), data=self.data)
        print(self.res.content)
        self.content = json.loads(self.res.content)
        result = []
        for i in range(0, len(self.content["data"]["list"]) - 1):
            result.append(self.content["data"]["list"][i]["company_name"])
        return result


class baidu(object):
    def __init__(self):
        self.url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%B9%BF%E5%B7%9E%E8%A7%86%E6%BA%90%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8"

        self.bananer = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
            "Cookie": "BAIDUID=A8AC42B1F46CDE7379A037C75CB62819:FG=1; BIDUPSID=A8AC42B1F46CDE7379A037C75CB62819; PSTM=1509928743; BDSFRCVID=W2AsJeCCxG3wqIbA3H_73bWlRYwArbZtRVBJ3J; H_BDCLCKID_SF=tRk8oDDafCvbfP0k54r-hICShUFX5-CsQbrCQhcH0hOWsIO6KfrDLjtnBNte5qbQLH5f54otytbCSlo_DUC0-nDSHHK8Jj8O3J; BD_UPN=123353; H_PS_645EC=87d0k6j1zJCm9Ri%2Fyz1u3cOEnpeK5T6s2yB7SB5VJZU3itkGx%2FAeu%2BGEwAs; BD_CK_SAM=1; PSINO=2; BDSVRTM=159; H_PS_PSSID=1426_12896_21106_17001_24879; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598"

        }
        self.proxies = {"http": "127.0.0.1:1080"}

    def save_txt(self, url):
        file = open("butians.txt", "a+")
        file.write("%s\n" % url)
        file.close()

    def connect_baidu(self, url):
        self.url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%s" % url
        self.res = requests.get(self.url, headers=self.bananer, timeout=10)
        self.soup = BeautifulSoup(self.res.content, 'html.parser')
        self.divs = self.soup.find_all('div', class_="f13")
        self.lis = self.divs[0].find('a', class_="c-showurl")
        try:
            baidulink = self.lis['href']
            res_url = requests.get(baidulink, allow_redirects=True, timeout=10)
            _url = res_url.url
        except:
            end_url = ""
            return end_url
        end_url = _url.split("/")[0] + "//" + _url.split("/")[2]
        return end_url

if __name__ == "__main__":
    for page in range(1,500):
        xxs = butian(page)
        for t in xxs.butianjson():
            xxa = baidu()
            baiduspider = xxa.connect_baidu(t)
            xxa.save_txt(baiduspider)
            print("FILE OK! %s" % baiduspider)