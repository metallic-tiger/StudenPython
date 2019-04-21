#!/usr/bin/python3          
# -*- coding: UTF-8 -*-     

#1.引入Tk模块
import tkinter 

#建立窗口类
windown=tkinter.Tk()

windown.title('显示在窗口上的标题')
windown.geometry('600x400')#窗口的长和宽
windown.attributes('-alpha',0.9)#设置窗口透明度为50% 似乎无效
def command():
    windown.quit()#退出消息循环
    

按钮=tkinter.Button(windown,text="按钮上显示的文字：退出",command =command)
按钮.place(x=200,y=200)

#显示窗口以及在这个上面的控件
#进入消息循环 消息循环只会执行设置好的消息内容
#例如 按钮的点击等等
windown.mainloop()
windown.destroy()#销毁窗口
#点击 x 标示退出也算退出消息循环
print('退出窗口之后执行的语句')
