#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import tkinter as tk  # 使用Tkinter前需要先导入
def windown() :
    # 实例化object，建立窗口window
    window = tk.Tk()
    window.title('My Window')
    window.geometry('500x300')  # 这里的乘是小x
    var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上

    # 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
    
    #textvariable这个标签指定 text的值为var
    l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
    
    l.pack()
    
    # 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
    on_hit = False
    def hit_me():
        nonlocal on_hit #在函数之中使其更新 上一级的作用域的变量
        if on_hit == False:
            on_hit = True
            l
            var.set('you hit me') #用于将按钮产生的数据传出
        else:
            on_hit = False
            var.set('')

    
    # 第5步，在窗口界面设置放置Button按键
    b = tk.Button(window, text="提交", font=('Arial', 12), width=10, height=1, command=hit_me)
    b.pack()

    
    #第6步，主窗口循环显示
    window.mainloop()

    #第7步，退出窗口之后的行为
    print('Quit')    
    return 0

if __name__ == "__main__":
    
    print(windown())
