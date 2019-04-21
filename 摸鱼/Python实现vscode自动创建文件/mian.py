#!/usr/bin/python3
# -*- coding: UTF-8 -*-
 
import tkinter 
#产生主窗口
root = tkinter.Tk()

root.title('创建新程序文件')
root.geometry('800x600')

'''
语言列表的内容一栏
待任务完成之后转化成使用文件读入
'''
Launch=('C/C++','python3')
listb  = tkinter.Listbox(root)
for i in Launch:
    listb.insert(0,i)


listb.pack()
root.mainloop()
