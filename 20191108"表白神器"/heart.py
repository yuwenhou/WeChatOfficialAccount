import turtle as t


def go_to(x, y):
    t.up()
    t.goto(x, y)
    t.down()


def big_Circle(size):  # 函数用于绘制心的大圆
    for i in range(150):
        t.forward(size)
        t.right(0.3)


def small_Circle(size):  # 函数用于绘制心的小圆
    for i in range(210):
        t.forward(size)
        t.right(0.786)


def line(size):
    t.forward(51 * size)


def heart(x, y, size):
    go_to(x, y)
    t.left(150)
    t.begin_fill()
    line(size)
    big_Circle(size)
    small_Circle(size)
    t.left(120)
    small_Circle(size)
    big_Circle(size)
    line(size)
    t.end_fill()


def arrow():
    t.pensize(10)
    t.setheading(0)
    go_to(-400, 0)
    t.left(15)
    t.forward(150)
    go_to(339, 178)
    t.forward(150)


def arrowHead():
    t.pensize(1)
    t.color('red', 'red')
    t.begin_fill()
    t.left(120)
    t.forward(20)
    t.right(150)
    t.forward(35)
    t.right(120)
    t.forward(35)
    t.right(150)
    t.forward(20)
    t.end_fill()


def main():

    t.setup()
    t.screensize(1000, 600, )
    t.pensize(2)
    t.color('red', 'pink')
    t.getscreen().tracer(30, 0)  # 取消注释后，快速显示图案
    heart(200, 0, 1)  # 画出第一颗心，前面两个参数控制心的位置，函数最后一个参数可控制心的大小
    t.setheading(0)  # 使画笔的方向朝向x轴正方向
    heart(-80, -100, 1.5)  # 画出第二颗心
    arrow()  # 画出穿过两颗心的直线
    arrowHead()  # 画出箭的箭头
    go_to(100, -300)
    t.write("author：一行数据❤️你们", move=True, align="left", font=(None, 30, "normal"))
    t.done()


if __name__ == '__main__':
    main()
