
目录
=================

   * [一、python基础知识](#一python基础知识)
   
               * [1.1 列出5个python标准库](#11-列出5个python标准库)
               * [1.2 python2和python3的range（100）的区别](#12-python2和python3的range100的区别)
               * [1.3python2和python3区别？列举5个](#13python2和python3区别列举5个)
               * [1.4 请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行](#14-请列出你会的任意一种统计图条形图折线图等绘制的开源库第三方也行)
               * [1.5 提高python运行效率的方法](#15-提高python运行效率的方法)
               * [1.6 遇到bug如何处理](#16-遇到bug如何处理)
               * [1.7 简述python引用计数机制](#17-简述python引用计数机制)
               * [1.8 列举3条以上PEP8编码规范](#18-列举3条以上pep8编码规范)
   * [二、python数据类型](#二python数据类型)
               * [2.1 python内建数据类型有哪些](#21-python内建数据类型有哪些)
               * [2.2 a=（1，）b=(1)，c=("1") 分别是什么类型的数据？](#22-a1b1c1-分别是什么类型的数据)
               * [2.3 python传参数是传值还是传址？](#23-python传参数是传值还是传址)
               * [2.4 列出python中可变数据类型和不可变数据类型，并简述原理](#24-列出python中可变数据类型和不可变数据类型并简述原理)
               * [2.5 python中交换两个数值](#25-python中交换两个数值)
               * [2.6 生成0-100的随机数](#26-生成0-100的随机数)
               * [2.7 一行代码实现1--100之和](#27-一行代码实现1--100之和)
               * [2.8 保留两位小数](#28-保留两位小数)
               * [2.9 a="张明 98分"，用re.sub，将98替换为100](#29-a张明-98分用resub将98替换为100)
               * [2.10 单引号、双引号、三引号用法](#210-单引号双引号三引号用法)
               * [2.11 字符串转化大小写](#211-字符串转化大小写)
               * [2.12 用两种方法去空格 str = " what the problem"](#212-用两种方法去空格-str---what-the-problem)
               * [2.13 避免转义给字符串加哪个字母表示原始字符串？](#213-避免转义给字符串加哪个字母表示原始字符串)
               * [a="hello"和b="你好"编码成bytes类型](#ahello和b你好编码成bytes类型)
               * [2.14 列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]](#214-列表12345请使用map函数输出1491625并使用列表推导式提取出大于10的数最终输出1625)
               * [2.15 [1,2,3] [4,5,6]的结果是多少？](#215-123456的结果是多少)
               * [2.16 list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]](#216-list235496从小到大排序不许用sort输出234569)
               * [2.17 python中生成随机整数、随机小数、0--1之间小数方法](#217-python中生成随机整数随机小数0--1之间小数方法)
               * [2.18 s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"](#218-s--ajldjlajfdljfddd去重并从小到大排序输出adfjl)
               * [2.19 x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果](#219-xabcydefzdef分别求出xjoiny和xjoinz返回的结果)
               * [2.20 a = "  hehheh  ",去除收尾空格](#220-a----hehheh--去除收尾空格)
               * [2.21 1. python实现列表去重的方法(多种方法)](#221-1-python实现列表去重的方法多种方法)
               * [2.22 举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]](#222-举例sort和sorted对列表排序list0-13-1059)
               * [2.23 对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序](#223-对list排序foo---58049-4-20-282-4使用lambda函数从小到大排序)
               * [2.24 使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小](#224-使用lambda函数对list排序foo---58049-4-20-282-4输出结果为024889-2-4-4-5-20正数从小到大负数从大到小)
               * [2.25 列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]](#225-列表推导式求列表所有奇数并构造新列表a---1-2-3-4-5-6-7-8-9-10)
               * [2.26 两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]](#226-两个列表1579和2268合并为12236789)
               * [2.27 [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]](#227-123456一行代码展开该列表得出123456)
               * [2.28 请将[i for i in range(3)]改成生成器](#228-请将i-for-i-in-range3改成生成器)
               * [2.29 列表嵌套元组，分别按字母和数字排序foo = [("zs",19),("ll",54),("wa",17),("df",23)]](#229-列表嵌套元组分别按字母和数字排序foo--zs19ll54wa17df23)
               * [2.30 列表嵌套列表排序，年龄数字相同怎么办？foo = [("zs",19),("ll",54),("wa",17),("df",23),("xf",23)]](#230-列表嵌套列表排序年龄数字相同怎么办foo--zs19ll54wa17df23xf23)
               * [2.31根据字符串长度排序](#231根据字符串长度排序)
               * [2.32 字典如何删除键和合并两个字典](#232-字典如何删除键和合并两个字典)
               * [2.33 字典根据键从小到大排序](#233-字典根据键从小到大排序)
               * [2.34列表嵌套字典的排序，分别根据年龄和姓名排序foo = [{"name":"zs","age":19},{"name":"ll","age":54},{"name":"wa","age":17},{"name":"df","age":23}]](#234列表嵌套字典的排序分别根据年龄和姓名排序foo--namezsage19namellage54namewaage17namedfage23)
               * [2.35 使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}](#235-使用pop和del删除字典中的name字段dicnamezsage18)
               * [2.36 python字典和json字符串相互转化方法](#236-python字典和json字符串相互转化方法)
               * [2.37 求三个方法打印结果](#237-求三个方法打印结果)
               * [2.38 python中什么元素为假？](#238-python中什么元素为假)
               * [2.39 is和==有什么区别？](#239-is和有什么区别)
   * [三、python函数和方法](#三python函数和方法)
               * [3.1 如何在一个函数内部修改全局变量](#31-如何在一个函数内部修改全局变量)
               * [3.2 递归求和](#32-递归求和)
               * [3.3 举例说明zip（）函数用法](#33-举例说明zip函数用法)
               * [3.4 利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"](#34-利用collections库的counter方法统计字符串每个单词出现的次数kjalfjldsjaflhdsllfdhglahfblhlahlfh)
               * [3.6 filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]](#36-filter方法求出列表所有奇数并构造新列表a---1-2-3-4-5-6-7-8-9-10)
               * [3.7 fun(*args,<strong>kwargs)中的 * args,</strong> kwargs什么意思？](#37-funargskwargs中的--args-kwargs什么意思)
               * [3.8 用lambda函数实现两个数相乘](#38-用lambda函数实现两个数相乘)
               * [3.9 python中断言方法举例](#39-python中断言方法举例)
               * [3.10 写一段自定义异常代码](#310-写一段自定义异常代码)
               * [3.11 举例说明异常模块中try except else finally的相关意义](#311-举例说明异常模块中try-except-else-finally的相关意义)
               * [3.12 IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常](#312-ioerrorattributeerrorimporterrorindentationerrorindexerrorkeyerrorsyntaxerrornameerror分别代表什么异常)
               * [3.13 python中copy和deepcopy区别](#313-python中copy和deepcopy区别)
               * [3.14 简述any()和all()方法](#314-简述any和all方法)
   * [四、python面向对象](#四python面向对象)
               * [4.1 一句话解释什么样的语言能够用装饰器?](#41-一句话解释什么样的语言能够用装饰器)
               * [4.2 简述面向对象中__new__和__init__区别](#42-简述面向对象中__new__和__init__区别)
               * [4.3 列出几种魔法方法并简要介绍用途](#43-列出几种魔法方法并简要介绍用途)
               * [4.4 写一个单例模式](#44-写一个单例模式)
   * [五、python文件操作](#五python文件操作)
               * [5.1 简述with方法打开处理文件帮我我们做了什么？](#51-简述with方法打开处理文件帮我我们做了什么)
               * [5.2 用python删除文件和用linux命令删除文件方法](#52-用python删除文件和用linux命令删除文件方法)
               * [5.3 log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”](#53-log日志中我们需要用时间戳记录errorwarning等的发生时间请用datetime模块打印当前时间戳-2018-04-01-113854)
               * [5.4 r、r 、rb、rb 文件打开模式区别](#54-rrrbrb文件打开模式区别)
   * [六、python多任务](#六python多任务)
               * [6.1 谈下python的GIL](#61-谈下python的gil)
               * [6.2 简述多线程、多进程](#62-简述多线程多进程)
               * [6.3 简述乐观锁和悲观锁](#63-简述乐观锁和悲观锁)
   * [七、python网络](#七python网络)
               * [7.1 列出常见的状态码和意义](#71-列出常见的状态码和意义)
               * [7.2 分别从前端、后端、数据库阐述web项目的性能优化](#72-分别从前端后端数据库阐述web项目的性能优化)
               * [7.3 简述同源策略](#73-简述同源策略)
               * [7.4 简述cookie和session的区别](#74-简述cookie和session的区别)
               * [7.5 常见的网络传输协议](#75-常见的网络传输协议)
               * [7.6 HTTP请求中get和post区别](#76-http请求中get和post区别)
   * [八、正则表达式](#八正则表达式)
               * [8.1 <div>我要吃鸡</div>，用正则匹配出标签里面的内容（“我要吃鸡”），其中class的类名是不确定的](#81-我要吃鸡用正则匹配出标签里面的内容我要吃鸡其中class的类名是不确定的)
               * [8.2 正则表达式匹配中，（.<em>）和（.</em>?）匹配区别？](#82-正则表达式匹配中和匹配区别)
               * [8.3 字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"](#83-字符串a--not-404-found-张三-99-深圳每个词中间是空格用正则过滤掉英文和数字最终输出张三--深圳)
               * [8.4 正则re.complie作用](#84-正则recomplie作用)
               * [8.5 正则匹配，匹配日期2018-03-20](#85-正则匹配匹配日期2018-03-20)
               * [8.6 s="info:xiaoZhang 33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']](#86-sinfoxiaozhang-33-shandong用正则切分字符串输出info-xiaozhang-33-shandong)
               * [8.7 正则匹配以163.com结尾的邮箱](#87-正则匹配以163com结尾的邮箱)
               * [8.8 正则匹配不是以4和7结尾的手机号](#88-正则匹配不是以4和7结尾的手机号)
               * [8.9 正则表达式匹配第一个URL](#89-正则表达式匹配第一个url)
               * [8.10 正则匹配中文](#810-正则匹配中文)
   * [九、数据库](#九数据库)
               * [9.1 数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句](#91-数据表student有idnamescorecity字段其中name中的名字可有重复需要消除重复行请写sql语句)
               * [9.2 数据库优化查询方法](#92-数据库优化查询方法)
               * [9.3 简述Django的orm](#93-简述django的orm)
               * [9.4 列出常见MYSQL数据存储引擎](#94-列出常见mysql数据存储引擎)
               * [9.5 MyISAM 与 InnoDB 区别：](#95-myisam-与-innodb-区别)
               * [9.6 写5条常用sql语句](#96-写5条常用sql语句)
               * [9.7 简述mysql和redis区别](#97-简述mysql和redis区别)
               * [9.8 举例说明SQL注入和解决办法](#98-举例说明sql注入和解决办法)
               * [9.9 正则表达式匹配出](#99-正则表达式匹配出)
   * [十、Linux知识](#十linux知识)
               * [10.1 10个Linux常用命令](#101-10个linux常用命令)
               * [10.2 Linux命令重定向 &gt; 和 &gt;&gt;](#102-linux命令重定向--和-)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

# 一、python基础知识
##### 1.1 列出5个python标准库
- os：提供了不少与操作系统相关联的函数
- sys:   通常用于命令行参数
- re:   正则匹配
- math: 数学运算
- datetime:处理日期时间

##### 1.2 python2和python3的range（100）的区别
python2返回列表，python3返回迭代器，节约内存

##### 1.3python2和python3区别？列举5个

1、Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hi')

Python2 既可以使用带小括号的方式，也可以使用一个空格来分隔打印内容，比如 print 'hi'

2、python2 range(1,10)返回列表，python3中返回迭代器，节约内存

3、python2中使用ascii编码，python3中使用utf-8编码

4、python2中unicode表示字符串序列，str表示字节序列python3中str表示字符串序列，byte表示字节序列

5、python2中为正常显示中文，引入coding声明，python3中不需要

6、python2中是raw_input()函数，python3中是input()函数

##### 1.4 请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行
pychart、matplotlib

##### 1.5 提高python运行效率的方法
1、使用生成器，因为可以节约大量内存
2、循环代码优化，避免过多重复代码的执行
3、核心模块用Cython  PyPy等，提高效率
4、多进程、多线程、协程
5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率

##### 1.6 遇到bug如何处理
1、细节上的错误，通过print（）打印，能执行到print（）说明一般上面的代码没有问题，分段检测程序是否有问题，如果是js的话可以alert或console.log
2、如果涉及一些第三方框架，会去查官方文档或者一些技术博客。
3、对于bug的管理与归类总结，一般测试将测试出的bug用teambin等bug管理工具进行记录，然后我们会一条一条进行修改，修改的过程也是理解业务逻辑和提高自己编程逻辑缜密性的方法，我也都会收藏做一些笔记记录。
4、导包问题、城市定位多音字造成的显示错误问题

##### 1.7 简述python引用计数机制
python垃圾回收主要以引用计数为主，标记-清除和分代清除为辅的机制，其中标记-清除和分代回收主要是为了处理循环引用的难题。
引用计数算法
当有1个变量保存了对象的引用时，此对象的引用计数就会加1
当使用del删除变量指向的对象时，如果对象的引用计数不为1，比如3，那么此时只会让这个引用计数减1，即变为2，当再次调用del时，变为1，如果再调用1次del，此时会真的把对象进行删除

##### 1.8 列举3条以上PEP8编码规范
1、顶级定义之间空两行，比如函数或者类定义。
2、方法定义、类定义与第一个方法之间，都应该空一行
3、三引号进行注释
4、使用Pycharm、Eclipse一般使用4个空格来缩进代码

# 二、python数据类型
##### 2.1 python内建数据类型有哪些
整型--int
布尔型--bool
字符串--str
列表--list
元组--tuple
字典--dict

##### 2.2 a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
a是tuple元组
b是int整数
c是str字符串

##### 2.3 python传参数是传值还是传址？
Python中函数参数是引用传递（注意不是值传递）。对于不可变类型（数值型、字符串、元组），因变量不能修改，所以运算不会影响到变量自身；而对于可变类型（列表字典）来说，函数体运算可能会更改传入的参数变量。



##### 2.4 列出python中可变数据类型和不可变数据类型，并简述原理
- 不可变数据类型：数值型、字符串型string和元组tuple
不允许变量的值发生变化，如果改变了变量的值，相当于是新建了一个对象，而对于相同的值的对象，在内存中则只有一个对象（一个地址），如下图用id()方法可以打印对象的id

- 可变数据类型：列表list和字典dict；
允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址也不会变化，不过对于相同的值的不同对象，在内存中则会存在不同的对象，即每个对象都有自己的地址，相当于内存中对于同值的对象保存了多份，这里不存在引用计数，是实实在在的对象。

##### 2.5 python中交换两个数值
```python
a,b = 3,4
a,b = b,a
```
##### 2.6 生成0-100的随机数
random.random()生成0-1之间的随机小数，所以乘以100
```python
import random
res1 = random.random()*100
res2 = random.randint(0,100)
```
##### 2.7 一行代码实现1--100之和
```python
sum(range(1,101))
```

##### 2.8 保留两位小数
题目本身只有a="%.03f"%1.3335,让计算a的结果，为了扩充保留小数的思路，提供round方法（数值，保留位数）
```python
a = "%.03f"%1.3335
b = round(float(a),2)
```


##### 2.9 a="张明 98分"，用re.sub，将98替换为100
```python
import re
a = "张明 98分"
ret = re.sub(r"\d+","100",a)
print(ret)
```
##### 2.10 单引号、双引号、三引号用法
1、单引号和双引号没有什么区别，不过单引号不用按shift，打字稍微快一点。表示字符串的时候，单引号里面可以用双引号，而不用转义字符,反之亦然。

'She said:"Yes." ' or  "She said: 'Yes.' "
2、但是如果直接用单引号扩住单引号，则需要转义，像这样：
 ' She said:\'Yes.\' '
3、三引号可以直接书写多行，通常用于大段，大篇幅的字符串
"""
hello
world
"""

##### 2.11 字符串转化大小写
```python
str = "HHHHUuuu"
print(str.upper())
print(str.lower())
```
##### 2.12 用两种方法去空格 str = " what the problem"
```python
str = " what the problem"
res = str.replace(" ","")
list = str.split(" ")
res = "".join(list)

```

##### 2.13 避免转义给字符串加哪个字母表示原始字符串？
r , 表示需要原始字符串，不转义特殊字符
##### a="hello"和b="你好"编码成bytes类型
```python
a = b"hello"
b = "你好".encode()
```

##### 2.14 列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
map（）函数第一个参数是fun，第二个参数是一般是list，第三个参数可以写list，也可以不写，根据需求
```python
lis = [1,2,3,4,5]
def dota(x):
    return x**2
result = map(dota,lis)
result = [i for i in result if i > 10]
```

##### 2.15 [1,2,3]+[4,5,6]的结果是多少？
两个列表相加，等价于extend
```python
a = [1,2,3]
b = [4,5,6]
c = a+b
print(c)
-------->结果
[1,2,3,4,5,6]
```
##### 2.16 list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
利用min()方法求出最小值，原列表删除最小值，新列表加入最小值，递归调用获取最小值的函数，反复操作
```python
list=[2,3,5,4,9,6]
new = []
def get_min(list):
    a = min(list)
    list.remove(a)
    new_list.append(a)
    if len(list)>0:
        get_min(list)
    return new_list
new_list = get_min(list)
```


##### 2.17 python中生成随机整数、随机小数、0--1之间小数方法
随机整数：random.randint(a,b),生成区间内的整数
随机小数：习惯用numpy库，利用np.random.randn(5)生成5个随机小数
0-1随机小数：random.random(),括号中不传参

##### 2.18 s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
set去重，去重转成list,利用sort方法排序，reeverse=False是从小到大排
```
s = "ajldjlajfdljfddd"
s = list(set(s)).sort(reverse=False)
res = "".join(s)
```

##### 2.19 x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果
join()括号里面的是可迭代对象，x插入可迭代对象中间，形成字符串，结果一致
```python
x="abc"
y="def"
z=["d","e","f"]
m = x.join(y)
n = x.join(z)
print(m)
print(n)
----------->
dabceabcf
dabceabcf

```

##### 2.20 a = "  hehheh  ",去除收尾空格
```python
a = "  hehheh  "
a.strip()
```

##### 2.21 1. python实现列表去重的方法(多种方法)
方法1: 使用时set方法
方法2: 使用字典的fromkeys()去重
方法3: 常规方法for循环
方法4: 使用sort方法
```python
lst = [1,2,3,4,12,32,13,312,1,1,1,23,3]
# set
lst1 = list(set(lst))
# fromkeys()
lst2 = {}.fromkeys(lst).keys()
# for
lst3 = []
for item in lst:
    if item not in lst3:
        lst3.append(item)
# sort
lst4.sort(keyt=lst.index)
```
##### 2.22 举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]
list.sort在list基础上修改，无返回值
sorted有返回值是新的list
```python
list = [0,-1,3,-10,5,9]
list.sort(reverse=False)
list = [0,-1,3,-10,5,9]
res = sorted(list,reverse=False)
```
##### 2.23 对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序
```python
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
a = sorted(foo, key=lambda x:x)
```
##### 2.24 使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小
（传两个条件，x<0和abs(x)）
```python
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
a = sorted(foo, key=lambda x:(x<0,abs(x)))
```

##### 2.25 列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```python
res = [i for i in a if i%2==1]
```
##### 2.26 两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
extend可以将另一个集合中的元素逐一添加到列表中，区别于append整体添加
```python
list1 = [1,5,7,9]
list2 = [2,2,6,8]
list1.extend(list2)
list1.sort(reverse=False)
```

##### 2.27 [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
```python
a = [[1,2],[3,4],[5,6]]
x = [j for i in a for j in i]
#或者使用numpy
import numpy as np
b = np.array(a).flatten().tolist()
```
##### 2.28 请将[i for i in range(3)]改成生成器
生成器是特殊的迭代器，

1、列表表达式的[]改为（）即可变成生成器
2、函数在返回值得时候出现yield就变成生成器，而不是函数了；

```python
a = (i for i in range(3))
type(a)#---->generator
```
##### 2.29 列表嵌套元组，分别按字母和数字排序foo = [("zs",19),("ll",54),("wa",17),("df",23)]
```python
foo = [("zs",19),("ll",54),("wa",17),("df",23)]
a = sorted(foo, key=lambda x:x[1],reverse=True)
a = sorted(foo, key=lambda x:x[0])
```

##### 2.30 列表嵌套列表排序，年龄数字相同怎么办？foo = [("zs",19),("ll",54),("wa",17),("df",23),("xf",23)]
a = sorted(foo, key=lambda x:(x[1],x[0]),reverse=True)
a = sorted(foo, key=lambda x:x[0])

##### 2.31根据字符串长度排序
```python
s = ["ab","abc","a","djkj"]
b = sorted(s, key=lambda x:len(x))
s.sort(key=len)


```


##### 2.32 字典如何删除键和合并两个字典
```python
dic1 = ["dota2","LOL","PUBG","CF"]
dic2 = ["炉石传说","王者荣耀"]
# 删除 del
del dic["dota2"]
# 合并 update
dic1.update(dic2)
```

##### 2.33 字典根据键从小到大排序
```python
dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
# 根据键来排序
lis = sorted(dic.items(), key=lambda i:i[0], reverse=False)
dict(lis)

```
##### 2.34列表嵌套字典的排序，分别根据年龄和姓名排序foo = [{"name":"zs","age":19},{"name":"ll","age":54},{"name":"wa","age":17},{"name":"df","age":23}]

```python
foo = [{"name":"zs","age":19},{"name":"ll","age":54},
{"name":"wa","age":17},{"name":"df","age":23}]
#按年龄从大到小
a = sorted(foo,key=lambda x:x["age"],reverse = True)
# 按姓名从小到大
a = sorted(foo,key=lambda x:x["name"])
```


##### 2.35 使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
```python
dic={"name":"zs","age":18}
dic.pop("name")
del dic["age"]
```

##### 2.36 python字典和json字符串相互转化方法
json.dumps()字典转json字符串，json.loads()json转字典
```python
import json
dic = {"name":"zs"}
res = json.dumps(dic)
ret = json.loads(res)

```

##### 2.37 求三个方法打印结果
fn("one",1）直接将键值对传给字典；
fn("two",2)因为字典在内存中是可变数据类型，所以指向同一个地址，传了新的额参数后，会相当于给字典增加键值对
fn("three",3,{})因为传了一个新字典，所以不再是原先默认参数的字典
```python
def fn(k,v,dic={}):
    dic[k] = v
    print(dic)
fn("one",1)
fn("two",2)
fn("three",3,{})
```

##### 2.38 python中什么元素为假？
（0，空字符串，空列表、空字典、空元组、None, False）

##### 2.39 is和==有什么区别？
is：比较的是两个对象的id值是否相等，也就是比较俩对象是否为同一个实例对象。是否指向同一个内存地址
== ： 比较的两个对象的内容/值是否相等，默认会调用对象的eq()方法

# 三、python函数和方法
##### 3.1 如何在一个函数内部修改全局变量
在函数内部修改global声明，修改全局变量
```python
def dota2():
    global NEC
    NEC = 4
```

##### 3.2 递归求和
```python
def get_sum(num):
    if num > 1:
        res = num+get_sum(num-1)
    else:
        res = 0
    return res
res = get_sum(10)
print(res)
```

##### 3.3 举例说明zip（）函数用法
zip()函数在运算时，会以一个或多个序列（可迭代对象）做为参数，返回一个元组的列表。同时将这些序列中并排的元素配对。

zip()参数可以接受任何类型的序列，同时也可以有两个以上的参数;当传入参数的长度不同时，zip能自动以最短序列长度为准进行截取，获得元组。
```python
a = [1,2]
b = [3,4]
res = [i for i in zip(a,b)]
print(res)
------------>结果
[(1, 3), (2, 4)]

```
##### 3.4 利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
```python
from collections import Counter
a = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
res=Counter(a)
print(res)

```

##### 3.6 filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表
```python
a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def fn(a):
    return a%2==1
newlist = fliter(fn,a)
newlist = [i for i in newlist]
```

##### 3.7 fun(*args,**kwargs)中的 * args,** kwargs什么意思？
有时可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，声明时不会命名。
加了星号（* ）的变量args会存放所有未命名的变量参数，args为元组；而加** 的变量kwargs会存放命名参数，即形如key=value的参数， kwargs为字典。

##### 3.8 用lambda函数实现两个数相乘
```python
sum = lambda a,b:a*b
print(sum(6,7))
```

##### 3.9 python中断言方法举例

assert（）方法，断言成功，则程序继续执行，断言失败，则程序报错
```python
a = 3
assert(a>1)
print("断言成功，程序继续向西执行")
b = 3
assert(b<7)
print("断言失败，程序报错")
```
##### 3.10 写一段自定义异常代码
自定义异常用raise抛出异常
```python
def fn():
    try:
        for i in range(5):
            if i > 2:
                raise Exception(“数字大于2了”)
    except Exception as ret:
        print(ret)
fn()

```

##### 3.11 举例说明异常模块中try except else finally的相关意义
try..except..else没有捕获到异常，执行else语句

try..except..finally不管是否捕获到异常，都执行finally语句

##### 3.12 IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常
IOError：输入输出异常
AttributeError：试图访问一个对象没有的属性
ImportError：无法引入模块或包，基本是路径问题
IndentationError：语法错误，代码没有正确的对齐
IndexError：下标索引超出序列边界
KeyError:试图访问你字典里不存在的键
SyntaxError:Python代码逻辑语法出错，不能执行
NameError:使用一个还未赋予对象的变量

##### 3.13 python中copy和deepcopy区别
1.复制不可变数据类型，不管copy还是deepcopy,都是同一个地址当浅复制的值是不可变对象（数值，字符串，元组）时和=“赋值”的情况一样，对象的id值与浅复制原来的值相同。

2、复制的值是可变对象（列表和字典）
浅拷贝copy有两种情况：
第一种情况：复制的 对象中无 复杂 子对象，原来值的改变并不会影响浅复制的值，同时浅复制的值改变也并不会影响原来的值。原来值的id值与浅复制原来的值不同。
第二种情况：复制的对象中有 复杂 子对象 （例如列表中的一个子元素是一个列表）， 改变原来的值 中的复杂子对象的值  ，会影响浅复制的值。
深拷贝deepcopy：完全复制独立，包括内层列表和字典

##### 3.14 简述any()和all()方法
any():只要迭代器中有一个元素为真就为真
all():迭代器中所有的判断项返回都是真，结果才为真

# 四、python面向对象
##### 4.1 一句话解释什么样的语言能够用装饰器?
函数可以作为参数传递的语言，可以使用装饰器

##### 4.2 简述面向对象中__new__和__init__区别
__init__是初始化方法，创建对象后，就立刻被默认调用了，可接收参数，如图

1、__new__至少要有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别

2、__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类（通过super(当前类名, cls)）__new__出来的实例，或者直接是object的__new__出来的实例

3、__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值

4、如果__new__创建的是当前类的实例，会自动调用__init__函数，通过return语句里面调用的__new__函数的第一个参数是cls来保证是当前类实例，如果是其他类的类名，；那么实际创建返回的就是其他类的实例，其实就不会调用当前类的__init__函数，也不会调用其他类的__init__函数。

##### 4.3 列出几种魔法方法并简要介绍用途
__init__:对象初始化方法
__new__:创建对象时候执行的方法，单列模式会用到
__str__:当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
__del__:删除对象执行的方法

##### 4.4 写一个单例模式
举个常见的单例模式例子，我们日常使用的电脑上都有一个回收站，在整个操作系统中，回收站只能有一个实例，整个系统都使用这个唯一的实例，而且回收站自行提供自己的实例。因此回收站是单例模式的应用。

确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，这个类称为单例类，单例模式是一种对象创建型模式。
```python
# 实例化一个单例
class Singleton(object):
    __instance = None

    def __new__(cls, age, name):
        #如果类数字能够__instance没有或者没有赋值
        #那么就创建一个对象，并且赋值为这个对象的引用，保证下次调用这个方法时
        #能够知道之前已经创建过对象了，这样就保证了只有1个对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

a = Singleton(18, "dongGe")
b = Singleton(8, "dongGe")

print(id(a))
print(id(b))

a.age = 19 #给a指向的对象添加一个属性
print(b.age)#获取b指向的对象的age属性
```

# 五、python文件操作
##### 5.1 简述with方法打开处理文件帮我我们做了什么？
打开文件在进行读写的时候可能会出现一些异常状况，如果按照常规的f.open

写法，我们需要try,except,finally，做异常判断，并且文件最终不管遇到什么情况，都要执行finally f.close()关闭文件，with方法帮我们实现了finally中f.close
##### 5.2 用python删除文件和用linux命令删除文件方法
- python：os.remove(文件名)
- linux:       rm  文件名

##### 5.3 log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”

```python
import time
print(strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
```
##### 5.4 r、r+、rb、rb+文件打开模式区别
"""
访问模式   读写状态        指针
r         只读          放在开头
w         写入          若无文件，创建新文件
a         打开追加       放在末尾，创建新的文件
rb        二进制只读      文件开头
wb        二进制写入      文件将其覆盖
ab        二进制追加      放在结尾，创建新文件
r+        读写           指针放在开头
w+        读写           文件将其覆盖
a+        读写           指针放在结尾，创建新的文件
rb+       二进制读写       指针放在开头
wb+       二进制读写       文件覆盖，创建新文件
ab+       二进制追加       放在结尾，如果不存在，创建新文件

"""
# 六、python多任务
##### 6.1 谈下python的GIL
GIL 是python的全局解释器锁，同一进程中假如有多个线程运行，一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。所以在多线程中，线程的运行仍是有先后顺序的，并不是同时进行。多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个python解释器，所以多进程可以实现多个进程的同时运行，缺点是进程系统资源开销大

##### 6.2 简述多线程、多进程
进程：
1、操作系统进行资源分配和调度的基本单位，多个进程之间相互独立
2、稳定性好，如果一个进程崩溃，不影响其他进程，但是进程消耗资源大，开启的进程数量有限制

线程：
1、CPU进行资源分配和调度的基本单位，线程是进程的一部分，是比进程更小的能独立运行的基本单位，一个进程下的多个线程可以共享该进程的所有资源
2、如果IO操作密集，则可以多线程运行效率高，缺点是如果一个线程崩溃，都会造成进程的崩溃

应用：
IO密集的用多线程，在用户输入，sleep 时候，可以切换到其他线程执行，减少等待的时间
CPU密集的用多进程，因为假如IO操作少，用多线程的话，因为线程共享一个全局解释器锁，当前运行的线程会霸占GIL，其他线程没有GIL，就不能充分利用多核CPU的优势

##### 6.3 简述乐观锁和悲观锁

- 悲观锁, 就是很悲观，每次去拿数据的时候都认为别人会修改，所以每次在拿数据的时候都会上锁，这样别人想拿这个数据就会block直到它拿到锁。传统的关系型数据库里边就用到了很多这种锁机制，比如行锁，表锁等，读锁，写锁等，都是在做操作之前先上锁。

- 乐观锁，就是很乐观，每次去拿数据的时候都认为别人不会修改，所以不会上锁，但是在更新的时候会判断一下在此期间别人有没有去更新这个数据，可以使用版本号等机制，乐观锁适用于多读的应用类型，这样可以提高吞吐量


# 七、python网络
##### 7.1 列出常见的状态码和意义
200 OK 
请求正常处理完毕
204 No Content 
请求成功处理，没有实体的主体返回
206 Partial Content 
GET范围请求已成功处理
301 Moved Permanently 
永久重定向，资源已永久分配新URI
302 Found 
临时重定向，资源已临时分配新URI
303 See Other 
临时重定向，期望使用GET定向获取
304 Not Modified 
发送的附带条件请求未满足
307 Temporary Redirect 
临时重定向，POST不会变成GET
400 Bad Request 
请求报文语法错误或参数错误
401 Unauthorized 
需要通过HTTP认证，或认证失败
403 Forbidden 
请求资源被拒绝
404 Not Found 
无法找到请求资源（服务器无理由拒绝）
500 Internal Server Error 
服务器故障或Web应用故障
503 Service Unavailable 
服务器超负载或停机维护

##### 7.2 分别从前端、后端、数据库阐述web项目的性能优化

- 前端优化：

1、减少http请求、例如制作精灵图
2、html和CSS放在页面上部，javascript放在页面下面，因为js加载比HTML和Css加载慢，所以要优先加载html和css,以防页面显示不全，性能差，也影响用户体验差

- 后端优化：
1、缓存存储读写次数高，变化少的数据，比如网站首页的信息、商品的信息等。应用程序读取数据时，一般是先从缓存中读取，如果读取不到或数据已失效，再访问磁盘数据库，并将数据再次写入缓存。
2、异步方式，如果有耗时操作，可以采用异步，比如celery
3、代码优化，避免循环和判断次数太多，如果多个if else判断，优先判断最有可能先发生的情况

- 数据库优化：
1、如有条件，数据可以存放于redis，读取速度快
2、建立索引、外键等

##### 7.3 简述同源策略
 同源策略需要同时满足以下三点要求： 

1）协议相同 
2）域名相同 
3）端口相同 
 http:www.test.com与https:www.test.com 不同源——协议不同 
 http:www.test.com与http:www.admin.com 不同源——域名不同 
 http:www.test.com与http:www.test.com:8081 不同源——端口不同
 只要不满足其中任意一个要求，就不符合同源策略，就会出现“跨域”
##### 7.4 简述cookie和session的区别
1，session 在服务器端，cookie 在客户端（浏览器）
2、session 的运行依赖 session id，而 session id 是存在 cookie 中的，也就是说，如果浏览器禁用了 cookie ，同时 session 也会失效，存储Session时，键与Cookie中的sessionid相同，值是开发人员设置的键值对信息，进行了base64编码，过期时间由开发人员设置
3、cookie安全性比session差

##### 7.5 常见的网络传输协议
UDP、TCP、FTP、HTTP、SMTP等等

##### 7.6 HTTP请求中get和post区别
1、GET请求是通过URL直接请求数据，数据信息可以在URL中直接看到，比如浏览器访问；而POST请求是放在请求头中的，我们是无法直接看到的；
2、GET提交有数据大小的限制，一般是不超过1024个字节，而这种说法也不完全准确，HTTP协议并没有设定URL字节长度的上限，而是浏览器做了些处理，所以长度依据浏览器的不同有所不同；POST请求在HTTP协议中也没有做说明，一般来说是没有设置限制的，但是实际上浏览器也有默认值。总体来说，少量的数据使用GET，大量的数据使用POST。
3、GET请求因为数据参数是暴露在URL中的，所以安全性比较低，比如密码是不能暴露的，就不能使用GET请求；POST请求中，请求参数信息是放在请求头的，所以安全性较高，可以使用。在实际中，涉及到登录操作的时候，尽量使用HTTPS请求，安全性更好。

# 八、正则表达式
##### 8.1 <div class="nam">我要吃鸡</div>，用正则匹配出标签里面的内容（“我要吃鸡”），其中class的类名是不确定的
```python
import re
str = "<div class="man">我要吃鸡</div>"
res = re.findall(r"<div class=".*>(.*?)</div>",str)
print(res)
```

##### 8.2 正则表达式匹配中，（.*）和（.*?）匹配区别？
- （.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配
- （.*?）是非贪婪匹配，会把满足正则的尽可能少匹配


##### 8.3 字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"

```python
import re
str = "not 404 found 张三 99 深圳"
list = str.split(" ")
print(list)
# 匹配数字和单词的表达式
res = re.findall("\d+|[a-zA-Z]+",str)
for i in res:
    if i in list:
        list.remove(i)
new_str = " ".join(list)
```

##### 8.4 正则re.complie作用
re.compile是将正则表达式编译成一个对象，加快速度，并重复使用

##### 8.5 正则匹配，匹配日期2018-03-20
```python
import re
url ='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
res = re.findall(r"dateRange=(.*?)%7C(.*?)&",url)
print(result)

```
##### 8.6 s="info:xiaoZhang 33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']
|表示或，根据冒号或者空格切分
```python
s="info:xiaoZhang 33 shandong"
res = re.split(r":|",s)
```
##### 8.7 正则匹配以163.com结尾的邮箱
```python
email_list = ["xiang@163.com","xianglal@qq.com","xiangdaad@123.com"]
for email in email_list:
    ret = re.match("[\w]{4,20}@163\.com$",email)
    if ret:
        print(ret)
```
##### 8.8 正则匹配不是以4和7结尾的手机号
```python
tels = ["13832428912","17233481392","10086","18000300007777"]
for tel in tels:
    ret = re.match("1\d{9}[0-3,5-6,8-9]",tel)
    if ret:
        print(ret)

```

##### 8.9 正则表达式匹配第一个URL
findall结果无需加group(),search需要加group()提取
```python
s = "sadbifshttps://www.baidu.com"
res = re.findall(r"https://.*?.com",s)[0]
res = re.search(r"https://.*?.com",s).group()
```
#####  8.10 正则匹配中文
```python
title = "你好，hello,我要吃鸡"
patter = re.compile(r'[\u4e00-\u9fa5]+')
result = pattern.findall(title)
```


# 九、数据库
##### 9.1 数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句
` select  distinct  name  from  student`

##### 9.2 数据库优化查询方法
外键、索引、联合查询、选择特定字段等等
##### 9.3 简述Django的orm
ORM，全拼Object-Relation Mapping，意为对象-关系映射
实现了数据模型与数据库的解耦，通过简单的配置就可以轻松更换数据库，而不需要修改代码只需要面向对象编程,orm操作本质上会根据对接的数据库引擎，翻译成对应的sql语句,所有使用Django开发的项目无需关心程序底层使用的是MySQL、Oracle、sqlite....，如果数据库迁移，只需要更换Django的数据库引擎即可

##### 9.4 列出常见MYSQL数据存储引擎
InnoDB：支持事务处理，支持外键，支持崩溃修复能力和并发控制。如果需要对事务的完整性要求比较高（比如银行），要求实现并发控制（比如售票），那选择InnoDB有很大的优势。如果需要频繁的更新、删除操作的数据库，也可以选择InnoDB，因为支持事务的提交（commit）和回滚（rollback）。 

MyISAM：插入数据快，空间和内存使用比较低。如果表主要是用于插入新记录和读出记录，那么选择MyISAM能实现处理高效率。如果应用的完整性、并发性要求比 较低，也可以使用。

MEMORY：所有的数据都在内存中，数据的处理速度快，但是安全性不高。如果需要很快的读写速度，对数据的安全性要求较低，可以选择MEMOEY。它对表的大小有要求，不能建立太大的表。所以，这类数据库只使用在相对较小的数据库表。

##### 9.5 MyISAM 与 InnoDB 区别：

1、InnoDB 支持事务，MyISAM 不支持，这一点是非常之重要。事务是一种高级的处理方式，如在一些列增删改中只要哪个出错还可以回滚还原，而 MyISAM就不可以了；
2、MyISAM 适合查询以及插入为主的应用，InnoDB 适合频繁修改以及涉及到安全性较高的应用；
3、InnoDB 支持外键，MyISAM 不支持；
4、对于自增长的字段，InnoDB 中必须包含只有该字段的索引，但是在 MyISAM表中可以和其他字段一起建立联合索引；
5、清空整个表时，InnoDB 是一行一行的删除，效率非常慢。MyISAM 则会重建表；

##### 9.6 写5条常用sql语句
show databases;
show tables;
desc 表名;
select * from 表名;
delete from 表名 where id=5;
update students set gender=0,hometown="北京" where id=5

##### 9.7 简述mysql和redis区别
redis： 内存型非关系数据库，数据保存在内存中，速度快
mysql：关系型数据库，数据保存在磁盘中，检索的话，会有一定的Io操作，访问速度相对慢

##### 9.8 举例说明SQL注入和解决办法
当以字符串格式化书写方式的时候，如果用户输入的有;+SQL语句，后面的SQL语句会执行，比如例子中的SQL注入会删除数据库demo
```python
# sql注入
input = "zs; drop database demo"
sql = 'select * from demo where name = ' + input
```
解决方式：通过传参数方式解决SQL注入
```python
# sql注入
input = "zs; drop database demo"
sql = "select * from demo where name = %s "%input
```
##### 9.9 正则表达式匹配出<hatml><h1>www.itcast.cn</h1></html>
前面的<>和后面的<>是对应的，可以用此方法
```python
labels = ["<html><h1>www.itcast.cn</h1></html>","<html><h1>www.itcast.cn</h1></html>"]
for i in labels:
    ret = re.match(r"<(\w*)><(\w*)>.*?</\2></\1>",i)
    if ret:
        print(ret.group())

```

# 十、Linux知识
##### 10.1 10个Linux常用命令
`ls  pwd  cd  touch  rm  mkdir  tree  cp  mv  cat  more  grep  echo `

##### 10.2 Linux命令重定向 > 和 >>

Linux 允许将命令执行结果 重定向到一个 文件
将本应显示在终端上的内容 输出／追加 到指定文件中
> 表示输出，会覆盖文件原有的内容
>> 表示追加，会将内容追加到已有文件的末尾

用法示例：
将 echo 输出的信息保存到 1.txt 里echo Hello Python > 1.txt
将 tree 输出的信息追加到 1.txt 文件的末尾tree >> 1.txt




### 
参考：
https://mp.weixin.qq.com/s/SyC_LLQL8AU3i6wYNlOdNQ
https://github.com/kenwoodjw/python_interview_question
