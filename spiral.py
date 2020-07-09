"""递归的应用——螺旋线"""
import turtle

def spiral(line_len):
    if line_len > 0: # 基本结束条件
        t.forward(line_len)
        t.right(90)
        spiral(line_len - 5)
        
 spiral(75)
 turtle.done()
