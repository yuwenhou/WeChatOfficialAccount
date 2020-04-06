import requests
from fake_useragent import UserAgent
from urllib import parse


class htmlDownload():
    '''
    下载 html 模块
    '''
    def get_html(self,pn,position_url,city,job):
        '''
        下载 html
        :param url:
        :return: response
        '''
        kw = job
        city = parse.quote(city)  # 编码为 url 的形式
        job = parse.quote(job)
        while True: # 防止代理失败
            try:
                while True:
                    headers = {
                        'User-Agent': UserAgent().random,
                        'Host' : 'www.lagou.com',
                        'Referer' : 'https://www.lagou.com/jobs/list_{}?&px=default&city={}'.format(job,city),
                        'X-Anit-Forge-Code' : '0',
                        'X-Anit-Forge-Token' : 'None',
                        'X-Requested-With' : 'XMLHttpRequest',
                    }

                    # 访问请求头中 Referer 键对应的 url 获得请求的 cookie ，实际请求 ajax url 时需带上
                    url = headers['Referer']
                    cookies = self.get_cookie(url,job,city)

                    # ajax 的 url 及表单数据
                    url = position_url.format(city)
                    data = {
                        'first': 'False',
                        'pn': pn,
                        'kd': kw
                    }

                    # 获得代理
                    proxies = self.get_proxies()

                    response = requests.post(url,headers=headers,data=data,cookies=cookies,proxies=proxies)
                    if response.status_code == 200:
                        response.encoding = 'utf-8'
                        return response
            except:
                continue

    def get_cookie(self,url,job,city):
        '''
        请求获得 cookie
        :return:
        '''
        while True: # 防止代理失败
            try:
                proxies = self.get_proxies()
                headers = {
                    'User-Agent': UserAgent().random,
                    'Host': 'www.lagou.com',
                    'Referer': 'https://www.lagou.com/jobs/list_{}?&px=default&city={}'.format(job, city),
                    'X-Anit-Forge-Code': '0',
                    'X-Anit-Forge-Token': 'None',
                    'X-Requested-With': 'XMLHttpRequest'
                }
                while True:
                    response = requests.get(url,headers=headers,proxies=proxies)
                    if response.status_code == 200:
                        cookies = response.cookies
                        return cookies
            except:
                continue

    def get_proxies(self):
        '''
        获得代理，阿布云代理
        https://center.abuyun.com
        :return:
        '''

        # 代理服务器
        proxyHost = "http-dyn.abuyun.com"
        proxyPort = "9020"

        # 代理隧道验证信息
        proxyUser = 'HZ2871E6G95IIA0D'
        proxyPass = 'A13E84D087B5ACE7'

        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }

        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }

        return  proxies