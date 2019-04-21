#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#输入地址 和 文件名
def MakePythonScript(add,FileName):
    #第一个是文件所在的地址，第二个是文件的名字
    Tempate=open(add+FileName+'.py','w')
    Tempate.writelines('#!/usr/bin/python3          \n' )
    Tempate.writelines('# -*- coding: UTF-8 -*-     \n')
    Tempate.writelines('\n\n')
    Tempate.close()

if __name__ == "__main__":
    add=input('地址为')
    filename=input('文件名为：')
    MakePythonScript(add,filename)
