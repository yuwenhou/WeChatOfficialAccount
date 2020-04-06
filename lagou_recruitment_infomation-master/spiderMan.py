from urlManager import urlManager
from htmlDownload import htmlDownload
from parseData import parseData
from dataOutput import  dataOutput


class spiderMan():
    '''
    爬虫主模块
    '''
    def __init__(self):
        '''
        初始化各个模块
        '''
        self.manager = urlManager()
        self.download = htmlDownload()
        self.parse = parseData()
        self.ouput = dataOutput()

    def start(self,city,job):
        '''
        开始爬取
        :return:
        '''
        # 创建 csv 文件
        self.ouput.create_csv(city,job)
        # 爬 30 页
        position_url = self.manager.get_position_url()
        for pn in range(1,31):

            '''
            买的是动态代理，使用时发现，代理虽然换了，但也常被封，可能是这个代理别人
            也拿去爬拉勾了，所以只要失败就重新换代理再请求
            '''
            while True:
                response = self.download.get_html(pn,position_url,city,job)
                if 'true' not in response.text:
                    continue
                else:
                    break

            data = self.parse.get_info(response.text)

            if data == None: # 编码错误的页跳过
                continue

            if data == []:
                print('\n爬取完毕或拉勾上此城市没有相关的职位！！！')
                break
            self.ouput.write_to_csv(data,city,job)

            print('\r第 {} 已爬取'.format(str(pn)),end='')

        print('\n爬取完毕，正在生成职位信息报表.....')


if __name__ == '__main__':
    '''
    主接口
    '''
    city = input('输入城市名：')
    job = input('输入职位名：')
    spider = spiderMan()
    spider.start(city,job)
    spider.ouput.create_table(city,job) # 生成报表
    print('\n职位报表生成完毕！')