#!/usr/bin/python3
# -*- coding:utf-8 -*-
import tkinter as tk
import tkinter.messagebox  # 要使用messagebox先要导入模块


function={
'<Button-1>' :'鼠标按钮n被按下，n为1左键，2中键，3右键',
'<ButtonRelease-1>': '鼠标按钮n被松开',
'<Double-Button-1>': '鼠标按钮n被双击',
'<Triple-Button-1>': '鼠标按钮n被三击',
'<Motion>': '鼠标在上面发生移动',
'<B1-Motion>': '鼠标按钮n被按下，同时，鼠标发生移动',
'<Enter>':'鼠标进入',
'<Motion>':'鼠标移动'
#'<Leave>':'鼠标离开',#注意使用鼠标离开操作可能会产生大量信号【谨慎使用】
#'<MouseWheel>':'鼠标滚轮滚动',#没有成功
}

function2={
    #区分大小写
    #键盘事件将发送到当前拥有键盘焦点的窗口小部件
    #没有键盘焦点的控件将无法触发键盘事件
"<Any-KeyPress>":"任意键按下" ,# <KeyPress>      <Key>   #未成功
'<KeyRelease>':'任意键松开',
'<KeyPress-A> ':' 特定键A按下' ,#<Key-key>       <key>
'<KeyRelease-A>' :'特定键A松开',
'<Shift-Up>' :'Shift-Up键被同时按下，up可以换成其它键位',#                任意键按下
#用户按了Enter键。几乎可以绑定到键盘上的所有键。
#特殊键有cancel（break键）、backspace、tab、return（回车键）、
# shift_l（任意shift键）、control_l（任意control键）、alt_l（任意alt键）
# 、pause、caps_lock、escape、prior（page up）、next（page down）、
# end、home、left、up、right、down、print、insert、delete、
# f1、f2、f3、f4、f5、f6、f7、f8，f9，f10，f11，f12，
# num_lock，滚动_lock。

}
#定义触发事件引发的函数
def MakeWindown(A):
    Windown=tk.Tk()
    
    Windown.title(function[A])
    Windown.geometry('500x400')
    button = tk.Button(Windown,text=function[A])
    button.place(x=100,y=200)
    button.bind(A,p_label) 
    
    button2 = tk.Button(Windown,text='测试',width=10, height=1, command=p_label2)
    button2.place(x=100,y=350)
    
    Windown.mainloop() 

def MakeWindown2(A):
    Windown=tk.Tk()
    
    Windown.title(function2[A])
    Windown.geometry('500x400')
    T = tk.Text(Windown, height=3)
    T.place(x=100,y=200)
    T.bind(A,p_label) 
    
    button2 = tk.Button(Windown,text='测试',width=10, height=1, command=p_label2)
    button2.place(x=100,y=350)
    
    Windown.mainloop() 

def p_label(events): #事件必须跟一个参数
    print('hello')
    tk.messagebox.showinfo(title='Hi', message='你好！') 

def p_label2(): 
    print('hello')
    tk.messagebox.showinfo(title='Hi', message='你好！') 

# for i in function.keys():
#     print(function[i], i)
#     MakeWindown(i)

for i in function2.keys():
    print(function2[i], i)
    MakeWindown2(i)
