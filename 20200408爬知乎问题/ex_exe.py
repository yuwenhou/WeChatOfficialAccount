import tkinter as tk
import time
import pandas as pd
import requests
# from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
pandas_data = []


def getAnser(qid, offset):
    # 利用知乎API请求json数据
    # qid:知乎问题号
    # offset:第几页
    # 知乎API
    url = "https://www.zhihu.com/api/v4/questions/{}/answers?include=content&limit=20&offset={}&platform=desktop&sort_by=default".format(
        qid, offset)
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    return res.json()


def get_data(qid):
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
    df2.to_csv("book.csv", encoding="utf_8_sig")


def show_original_pic(text):
    """放入文件"""
    path = askdirectory(title='选择文件')
    text.delete(1.0, tk.END)
    text.tag_config('red', foreground='RED')
    text.insert(tk.END, path, 'red')


def main():
    root = tk.Tk()
    root.geometry("800x500")
    root.title("知乎书单爬虫：公众号：一行数据")

    la1 = tk.Label(root, text="知乎问题号:")
    la1.place(x=50, y=50, width=100)

    qid = tk.StringVar()
    question = tk.Entry(root, textvariable=qid)
    question.place(x=150, y=50)

    # 选择保存路径

    # 打开本地文件
    text = tk.Text(root, width=10, height=2)
    text.place(x=150, y=100)
    tk.Button(root, text='保存文件路径', command=lambda: show_original_pic(text)).place(x=60, y=100)

    # 设置评分标签
    la2 = tk.Label(root, text="保存文件名 :")
    la2.place(x=50, y=150, width=100)

    file_name = tk.StringVar()
    file = tk.Entry(root, textvariable=file_name)
    file.place(x=150, y=150)

    # 按钮
    paqv = tk.Button(root, text='开始爬取', bg="blue", fg="black", width=7, compound='center',
                     command=lambda: get_data(qid))
    paqv.place(x=50, y=250)

    tk.mainloop()


if __name__ == '__main__':
    main()
