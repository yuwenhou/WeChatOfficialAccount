import requests
import re
import pandas as pd
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
pandas_data = []

def getAnser(qid, offset):
    # 利用知乎API请求json数据
    # qid:知乎问题号
    # offset:第几页
    # 知乎API
    url = "https://www.zhihu.com/api/v4/questions/{}/answers?include=content&limit=20&offset={}&platform=desktop&sort_by=default".format(
        qid, offset)
    # https://www.zhihu.com/api/v4/questions/281789365/answers?include=content&limit=20&offset=20&platform=desktop&sort_by=default
    # https://www.zhihu.com/question/281789365
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    return res.json()


def getBooksAndAnswers(qid):
    # 获取所有书籍和回答数据
    offset = 0
    num = 0
    data2 = set()
    movie_data = {}
    while True:
        qid = qid
        print('Offset =', offset)
        # 知乎api请求
        data = getAnser(qid, offset)
        print(data)
        if len(data['data']) == 0:
            break
        for line in data['data']:
            # 保存回答数据
            content = line['content']
            result = re.findall(r'《(.*?)》', content)
            # if ips.empty():
            #     get_ip()
            for name in result:
                if "<a" in name:
                    name = name.split('>')[1].split("<")[0]
                print(name)
                if "<b" in name:
                    name = name.strip().replace("<b>", '').replace('</b>', '')
                if "<i" in name:
                    name = name.strip().replace('<i>', '').replace('</i>', '')
                movie_data[name] = movie_data.get(name, 0) + 1
                # try:
                #     douban_movie(name)
                # except Exception as e:
                #     print(traceback.format_exc())
        offset += 20
        time.sleep(1)
    for i in movie_data.keys():
        new_data = {}
        if i:
            new_data['书籍名称'] = i
            new_data['频率'] = movie_data[i]
            pandas_data.append(new_data)
    df2 = pd.DataFrame(pandas_data, columns=['书籍名称', '频率'])
    df2.to_csv("zhihu_book.csv")




# getBooksAndAnswers(281789365)
getBooksAndAnswers(270883846)


