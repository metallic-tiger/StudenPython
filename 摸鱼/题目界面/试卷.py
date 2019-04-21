#!/usr/bin/python3
# -*- coding: UTF-8 -*-

xz=[
        ['1、计算机中，信息是以哪种形式存储的'
        
        ]
]
import tkinter as tk
import mod
window=tk.Tk()
window.title('考试')
window.geometry('1000x800') 

xzt=[]
vars=[]
def  at(n):
    E=mod.XZ(xz[n])
    vars[n]=E[0]
    if E[1]==0:
        return
    elif E[1]==1:
        if n<=24:
            at(n+1)
        return
    elif n>0:
        at(n-1)
    else:
        pass


LB1=tk.
for  i in range(0,25):
    vars.append(tk.IntVar())
    xzt.append(tk.Button(window, textvariable=vars[i], font=('Arial', 12), width=4, height=1, command=lambda :at(i)))
    xzt[i].grid(row=i//10, column=i%10)


window.mainloop()
