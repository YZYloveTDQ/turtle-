"""分形树——理解递归的原理"""
import turtle

def fractal_tree(branch_len):
    """递归实现分形树"""
    if branch_len > 5: # 基本结束条件
        t.forward(branch_len)
        t.right(20)
        fractal_tree(branch_len - 15)
        # 一直循环递归到树枝长度<5
        # 循环停止后继续后面的操作（注意是回到停止的上一个循环）
        t.left(40)
        fractal_tree(branch_len - 15)
        
        t.right(20)
        t.backward(branch_len)
        

t.pencolor('green')
t.pensize(2)
t.left(90)
t.speed(1)
fractal_tree(75)
turtle.done()
