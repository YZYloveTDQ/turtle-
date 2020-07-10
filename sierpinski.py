import turtle

t = turtle.Turtle()

def get_middle(point1, point2):
    """计算两个坐标之间的中点, point1，point2都是存储坐标的元组"""
    return ((point1[0]+point2[0])/2, (point1[1]+point2[1])/2)


def draw_triangle(points, color):
    """绘制三角形，points是一个字典包含三个点的坐标"""
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()

def sierpinski(degree, points):
    """
    绘制谢尔宾斯基三角形
        degree：堆叠的次数
        points：原始三角形坐标(一个字典)
    """
    colormap = ['blue', 'red', 'green', 'white',
                'orange', 'yellow']  # 颜色列表，不同degree阶段用不同颜色

    # 第一次递归
    draw_triangle(points, colormap[degree])  # 绘制原始三角形

    if degree > 0:  # 基本结束条件
        # 先绘制左边三角形，再上三角形，最后右边三角形

        # 左边三角形
        # 左点与上一层三角形坐标一致
        # 顶点是上一层三角形左点和顶点的中点
        # 右点是上一层三角形左点和右点的中点
        sierpinski(degree-1, {
            'left': points['left'],
            'top': get_middle(points['left'], points['top']),
            'right': get_middle(points['left'], points['right'])
        })

        # 上三角形
        sierpinski(degree-1, {
            # 左点是上一层三角形的左点和顶点的中点
            'left': get_middle(points['left'], points['top']),
            'top': points['top'],  # 顶点坐标与上一层三角形顶点一致
            'right': get_middle(points['top'], points['right'])
        })

        # 右三角形
        sierpinski(degree-1, {
            'left': get_middle(points['left'], points['right']),
            'top': get_middle(points['top'], points['right']),
            'right': points['right']
        })

points = {
    'left': (-200, -100),
    'top': (0, 200),
    'right': (200, -100)
    }

sierpinski(5, points)
turtle.done()
