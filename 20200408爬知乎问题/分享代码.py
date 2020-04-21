import requests
import re
import pandas as pd

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
pandas_data = []

def getBooksAndAnswers(qid):
    # 获取所有书籍和回答数据
    offset = 0
    book_data = {}
    while True:
        qid = qid
        print('Offset =', offset)
        # 知乎api请求
        url = "https://www.zhihu.com/api/v4/questions/{}/answers?include=content&limit=20&offset={}&platform=desktop&sort_by=default".format(
            qid, offset)
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        data = res.json()
        if len(data['data']) == 0:
            break
        for line in data['data']:
            # 保存回答数据
            content = line['content']
            result = re.findall(r'《(.*?)》', content)
            for name in result:
                book_data[name] = book_data.get(name, 0) + 1
        offset += 20
    # 保存爬取的内容
    for i in book_data.keys():
        new_data = {}
        if i:
            new_data['书籍名称'] = i
            new_data['频率'] = book_data[i]
            pandas_data.append(new_data)
    df2 = pd.DataFrame(pandas_data, columns=['书籍名称', '频率'])
    df2.to_csv("book.csv",encoding="utf_8_sig")



getBooksAndAnswers(281789365)


