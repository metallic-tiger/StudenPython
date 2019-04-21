#!/usr/bin/python3          
# -*- coding: UTF-8 -*-  

import tkinter as tk
import tkinter.messagebox  # 要使用messagebox先要导入模块

def XZ(题目):
    #
    # 题目要求
    # 0 题干
    # 1.2.3.4均为选项
    # #
    windown=tk.Tk()

    windown.title('选择题')
    windown.geometry('600x400')#窗口的长和宽
    
    T=tk.Label(windown,text=题目[0], bg='white', font=('Arial', 12), width=45, height=4)
    T.place(x=100,y=25)

    var=tk.IntVar()#用于返回题目答案状态
    var2=tk.IntVar()  #用于返回 是进入下一题还是返回上一题还是退出

    var.set(-1)
    var2.set(0)

    def out():
        if var.get() !=-1:
            windown.quit()
        else:
            tkinter.messagebox.showinfo(title='Hi', message='还没有填题目哦')
        var2.set(0)

    def NextUp():
        if var.get() !=-1:
            windown.quit()
        else:
            tkinter.messagebox.showinfo(title='Hi', message='还没有填题目哦')
        var2.set(1)

    def NextBack():
        windown.quit()
        var2.set(-1) 

    RadioButtonList=[]
    for i in range(1,len(题目)):
        RadioButtonList.append(tk.Radiobutton(windown, text=题目[i], variable=var, value=i)) 
        RadioButtonList[i-1].place(x=150,y=90+i*30)
    
    


    B=tk.Button(windown, text="返回上一题", font=('Arial', 12), width=7, height=1, command=NextBack)
    B.place(x=80,y=140+len(题目)*30)
    B=tk.Button(windown, text="提交", font=('Arial', 12), width=7, height=1, command=out)
    B.place(x=250,y=140+len(题目)*30)
    B=tk.Button(windown, text="下一题", font=('Arial', 12), width=7, height=1, command=NextUp)
    B.place(x=420,y=140+len(题目)*30)
    windown.mainloop()
    windown.destroy()
    return (var.get(),var2.get())


#####################工作在本行
def TkT(题目):
    #
    # 题目要求
    # 0 题干
    # 1为需要填的空数量
    # #
    windown=tk.Tk()

    windown.title('填空题')
    windown.geometry('600x400')#窗口的长和宽
    
    T=tk.Label(windown,text=题目[0], bg='white', font=('Arial', 12), width=45, height=4)
    T.place(x=100,y=25)

    var=tk.IntVar()#用于返回题目状态
    var2=tk.IntVar()  #用于返回 是进入下一题还是返回上一题还是退出

    var.set("0")
    var2.set(0)

    def FULL():
        for i in range(0,题目[1]):
            if EntryList[i].get()=='':
                return 0
        return 1

    def out():
        if FULL():
            windown.quit()
        else:
            tkinter.messagebox.showinfo(title='Hi', message='还没有填完题目哦')
        var2.set(0)

    def NextUp():
        if FULL():
            windown.quit()
        else:
            tkinter.messagebox.showinfo(title='Hi', message='还没有填完题目哦')
        var2.set(1)

    def NextBack():
        if FULL():
            windown.quit()
        else:
            tkinter.messagebox.showinfo(title='Hi', message='还没有填完题目哦')
        var2.set(-1) 
    

    EntryList=[]
    LabelList=[]
    for i in range(0,题目[1]):
        LabelList.append(tk.Label(windown,text="第"+str(i+1)+"空：",  font=('Arial', 13), width=6, height=1))
        EntryList.append(tk.Entry(windown,show=None, font=('Arial', 14))) 
        LabelList[i].place(x=160,y=120+i*30)
        EntryList[i].place(x=220,y=120+i*30)
    
    


    B=tk.Button(windown, text="返回上一题", font=('Arial', 12), width=7, height=1, command=NextBack)
    B.place(x=80,y=140+题目[1]*30)
    B=tk.Button(windown, text="提交", font=('Arial', 12), width=7, height=1, command=out)
    B.place(x=250,y=140+题目[1]*30)
    B=tk.Button(windown, text="下一题", font=('Arial', 12), width=7, height=1, command=NextUp)
    B.place(x=420,y=140+题目[1]*30)
    windown.mainloop()
    massge=[]
    for i in range(0,题目[1]):
        massge.append(EntryList[i].get())

    windown.destroy()
    return (massge,var2.get())




