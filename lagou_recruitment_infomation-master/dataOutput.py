import csv
import os
import pandas as pd
from pyecharts.commons import utils # 执行 JavaScript 用
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Page, Pie
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType


class dataOutput():
    '''
    数据输出模块
    '''
    def create_csv(self,city,job):
        '''
        创建以‘城市+职位名’为名的 csv 文件，并写入头信息
        :return:
        '''
        with open(city + '_' + job + '.csv','w+',encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['职位名','公司名','公司规模','公司主要业务',
                             '融资情况','公司待遇福利','职位类型','技能要求',
                             '职位发布时间','行政区','薪水','工作经验',
                             '工作性质','学历要求'])

    def write_to_csv(self,data,city,job):
        '''
        写入 csv 文件
        :param data:
        :return:
        '''
        with open(city + '_' + job + '.csv','a+',encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            for dt in data:
                writer.writerow(dt)

    def create_table(self,city,job):
        '''
        生成报表
        :param city:
        :param job:
        :return:
        '''
        # 创建保存报表文件夹
        path = r'./' + city + '_' + job
        self.mkdir(path)

        df = pd.read_csv(open(city + '_' + job + '.csv',encoding='utf-8'))
        # 公司规模分布柱状图
        self.bar(df['公司规模'],"人数","公司人数规模分布",path)
        # 公司主要业务分布词云
        self.wordcloud(df['公司主要业务'],"公司业务词云图",path)
        # 融资情况柱状图
        self.bar(df['融资情况'],"数量","公司融资情况分布",path)
        # 公司待遇福利词云
        self.wordcloud(df['公司待遇福利'],"公司福利待遇词云图",path)
        # 技能要求词云图
        self.wordcloud(df['技能要求'],"技能要求词云图",path)
        # 行政区占比饼状图
        self.pie(df['行政区'],"岗位招聘地区分布比例",path)
        # 薪水分布柱状图，可水平拖动
        self.bar_level(df['薪水'],"数量","薪水区间分布状况",path)
        # 工作经验柱状图
        self.bar(df['工作经验'],"数量","工作经验要求分布",path)
        # 工作性质分布
        self.pie(df['工作性质'],"招聘性质占比",path)
        # 学历要求柱状图
        self.bar(df['学历要求'],"数量","招聘学历要求分布",path)

    def mkdir(self,path):
        '''
        创建保存报表的文件夹
        :param city:
        :param job:
        :return:
        '''
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
        else:
            # 如果目录存在则不创建，pass
            pass

    def bar(self,df,legend,title,path):
        '''
        柱状图
        :param df: 要操作的数据
        :param legend: 图例
        :param title: 报表标题
        :param path: 保存路径
        :return:
        '''
        tmp = df.value_counts()
        x = list(tmp.index)
        y = list(tmp)
        bar = Bar()
        bar.add_xaxis(x)
        bar.add_yaxis(legend, y, category_gap="60%")
        bar.set_series_opts(itemstyle_opts={
            "normal": {
                "color": utils.JsCode("""new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(0, 244, 255, 1)'
                        }, {
                            offset: 1,
                            color: 'rgba(0, 77, 167, 1)'
                        }], false)"""),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": 'rgb(0, 160, 221)',
            }})
        bar.set_global_opts(title_opts=opts.TitleOpts(title=title))
        bar.render(path + '/' + title + '.html')

    def wordcloud(self,df,title,path):
        '''
        词云图
        :param df:
        :param title:
        :return:
        '''
        # 统计关键字
        # 统计关键字
        tmp = {}
        for t in list(df):
            t = str(t)
            if '|' in t:
                t = t.replace('丨', ',')
            if '/' in t:
                t = t.replace('/', ',')
            if ' ' in t:
                t = t.replace(' ', ',')
            if '、' in t:
                t = t.replace('、', ',')
            if '，' in t:
                t = t.replace('，', ',')
            t = t.split(',')
            for _ in t:
                tmp[_] = tmp.get(_, 0) + 1

        words = list(tmp.items())
        c = (
            WordCloud()
                .add("", words, word_size_range=[20, 100])
                .set_global_opts(title_opts=opts.TitleOpts(title=title))
        )
        c.render(path + '/' + title + '.html')

    def pie(self,df,title,path):
        '''
        饼状图
        :param df:
        :param title:
        :param path:
        :return:
        '''
        tmp = df.value_counts()
        x = list(tmp.index)
        y = list(tmp)

        c = (
            Pie()
                .add("", [list(z) for z in zip(x, y)])
                .set_global_opts(title_opts=opts.TitleOpts(title=title))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
                .set_global_opts(
                legend_opts=opts.LegendOpts(pos_left="70%"),
            )
        )
        c.render(path + '/' + title + '.html')

    def bar_level(self,df,legend,title,path):
        '''
        薪水分布情况柱状图
        :param df:
        :param legend:
        :param title:
        :param path:
        :return:
        '''
        tmp = df.value_counts()
        x = list(tmp.index)
        y = list(tmp)

        c = (
            Bar()
                .add_xaxis(x)
                .add_yaxis(legend, y)
                .set_global_opts(
                title_opts=opts.TitleOpts(title=title),
                datazoom_opts=opts.DataZoomOpts(),
            )
        )
        c.render(path + '/' + title + '.html')