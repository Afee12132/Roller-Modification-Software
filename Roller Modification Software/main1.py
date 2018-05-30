# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:05:50 2018

@author: dell
"""

from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import *
import main3x1
import main3x2
import main3x3
import main3x4
import main3x5
import main3x6
import qjbl
qjbl.bl()

def info():
    '''软件信息介绍框'''
    show = showinfo(title="软件介绍",
                    message='''
                    本软件用于圆柱圆锥滚子的修形设计工作，能方便快捷的计算给
                    定工况下滚子的接触应力分布情况，为修形设计提供参考，大大
                    提高工作效率。
                    ''',)


def fun():
    f1.destroy()
    
    import main2
    main2.main2(root)
def fun1():
    tl = Toplevel()
    main3x1.func1(root,tl)
def fun2():
    tl = Toplevel()
    main3x2.func2(root,tl)
def fun3():
    tl = Toplevel()
    main3x3.func3(root,tl)
def fun4():
    tl = Toplevel()
    main3x4.func4(root,tl)
def fun5():
    tl = Toplevel()
    main3x5.func5(root,tl)
def fun6():
    tl = Toplevel()
    main3x6.func6(root,tl)   
    
    
    
    
root = Tk()
root.title('滚子修形分析系统')
root.resizable(width=False,height=False)
# 菜单栏
menu = Menu(root)   #相当于菜单栏
root.config(menu=menu)

filemenu = Menu(menu,tearoff=0)   #在菜单栏上添加新菜单
menu.add_cascade(label="新建", menu=filemenu)     #添加下拉菜单

filemenu.add_command(label="圆柱滚子直线型",command=fun1) #往菜单里添加新条目
filemenu.add_command(label="圆柱滚子圆弧型",command=fun2) #往菜单里添加新条目
filemenu.add_command(label="圆柱滚子对数型",command=fun3) #往菜单里添加新条目
filemenu.add_separator()  #画一条分割线
filemenu.add_command(label="圆锥滚子直线型",command=fun4) #往菜单里添加新条目
filemenu.add_command(label="圆锥滚子圆弧型",command=fun5) #往菜单里添加新条目
filemenu.add_command(label="圆锥滚子对数型",command=fun6) #往菜单里添加新条目
# =============================================================================
# filemenu.add_command(label="打开",)
# filemenu.add_separator()   #画一条分割线
# filemenu.add_command(label="保存",)
# =============================================================================
infomenu = Menu(menu,tearoff=0)
menu.add_cascade(label="关于", menu=infomenu)
infomenu.add_command(label="软件介绍",command=info)



f1=Frame(root)
f1.pack()
c1 = Canvas(f1,width=1000,height=600)
c1.pack()

img = ImageTk.PhotoImage(file = 'bjt1.jpg')
c1.create_image(0,0,anchor='nw',image=img)

c1.create_text(500,200,text='圆柱圆锥滚子修形分析系统',font=('黑体',50),
               fill='white')
c1.create_text(500,550,text='大连理工大学 - 机械工程学院',
               font=('黑体',20),fill='white')

b = Button(f1,text='新建项目',font=('黑体',20),fg='blue',command=fun)
b.place(relx=0.5,rely=0.6,anchor='center')
root.mainloop()

