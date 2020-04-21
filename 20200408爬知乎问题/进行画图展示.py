import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file_name = 'zhihu_5646book.csv'
df = pd.read_csv(file_name, encoding='utf-8')
df = df.sort_index(by = "频率",ascending = False)  

print(df.head())
print(df[1:10])

# 画图

#color = sns.color_palette('Paired', 16)
#plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
#plt.barh(range(10,0,-1),df["频率"][0:10],color = color)
#plt.yticks(range(10,0,-1),df["书籍名称"][0:10],fontsize=12)
## 设置字体大小，参数与Text一样
#plt.xlabel("推荐次数",fontsize=14)
#plt.ylabel("书籍名称",fontsize=14)
#plt.title("知乎5646回答-推荐书籍前十名")
## 设置边距
#plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.1)
#
#plt.show()
# 推荐书单
color = sns.color_palette('Paired', 16)
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.barh(range(10,0,-1),df["频率"][10:20],color = color)
plt.yticks(range(10,0,-1),df["书籍名称"][10:20],fontsize=12)
# 设置字体大小，参数与Text一样
plt.xlabel("推荐次数",fontsize=14)
plt.ylabel("书籍名称",fontsize=14)
plt.title("知乎5646回答-推荐书籍前11-20名")
# 设置边距
plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.1)

plt.show()

