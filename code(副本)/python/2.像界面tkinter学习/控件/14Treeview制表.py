import tkinter
from    tkinter import ttk

wuya = tkinter.Tk()
wuya.title("wuya")
wuya.geometry("900x200+10+20")

# 创建表格
tree_date = ttk.Treeview(wuya)

# 定义列
tree_date['columns'] = ['name','age','weight','number']
tree_date.pack()

# 设置列宽度
tree_date.column('name',width=100)
tree_date.column('age',width=100)
tree_date.column('weight',width=100)
tree_date.column('number',width=100)

# 添加列名
tree_date.heading('name',text='姓名')
tree_date.heading('age',text='年龄')
tree_date.heading('weight',text='体重')
tree_date.heading('number',text='工号')

# 给表格中添加数据
tree_date.insert('',0,text='date1',values=('大豆',21,'60kg','3121211034'))
tree_date.insert('',1,text='date2',values=('花生',21,'54kg','3121211033'))
tree_date.insert('',2,text='date3',values=('玉米',21,'65kg','3121211023'))
tree_date.insert('',3,text='date4',values=('土豆',21,'34kg','3121211053'))
tree_date.insert('',4,text='date5',values=('番茄',21,'65kg','3121211063'))
tree_date.insert('',6,text='date6',values=('高粱',21,'64kg','3121211073'))
# 第一个参数为第一层级，可能在这不太好理解，下篇文章中说到树状结构就理解了

wuya.mainloop()
