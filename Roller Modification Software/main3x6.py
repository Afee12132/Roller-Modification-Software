# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:21:29 2018

@author: dell
"""
import yzds
import numpy as np  
from tkinter import *
from PIL import Image, ImageTk   #tkinter本身只能打开gif格式，导入该模块可打开jpg或png
import qjbl

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

#qjbl.bl()
def func6(win,tl):
    qjbl.set_v('Dd',0)

####绘图函数###################################################
    def hui1():
        f1.clf()
        a1 = f1.add_subplot(111)
        s1 = qjbl.get_v('Dd')[:,int((int(Ys.get())+1)/2)]
        a1.plot(s1)
        canvas1.show()
        text1.set('图1 - 最大接触应力分布图'+'  F='+F.get()+'N')
    
       
        
    def hui2():
        f2.clf()
        a2 = f2.gca(projection='3d')
        x = np.arange(0, int(Xs.get()))
        y = np.arange(0, int(Ys.get()))
        X, Y = np.meshgrid(x, y)
        Z = qjbl.get_v('Dd').T
        # Plot the surface.
        surf = a2.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                             linewidth=0,)
        f2.colorbar(surf, shrink=0.5, aspect=10)
        canvas2.show()
        text2.set('图2 - 滚子接触应力三维分布图'+'  F='+F.get()+'N')
    #####################################################    
    
    ########################################
    # =============================================================================
    # root2 = Tk()
    # root2.title('滚子修形计算')
    # =============================================================================
    
    #tl = Toplevel()
    #tl.title('圆锥直线型修形')
    Fr = Frame(tl)
    Fr.grid()
    f1 = Frame(Fr)
    f1.grid(row=0,column=0,sticky=N,pady=20,)
    
    f1_1 = Frame(f1)
    f1_1.grid(row=0,column=0,pady=2,padx=20,sticky=N+W)
    
    ll = Label(f1_1,text='参数设置',font=('黑体',15))
    ll.grid(row=0,column=0,padx=20,pady=2,sticky=W+N)
    
    l1 = Label(f1_1,text='滚子长度 L',font=(10))
    l1.grid(row=1,column=0,padx=20,pady=8,sticky=W)
    cd = StringVar()
    cd.set(20)
    e1 = Entry(f1_1,textvariable=cd,)
    e1.grid(row=1,column=1)
    l1_1 = Label(f1_1,text='mm',font=(10))
    l1_1.grid(row=1,column=2,pady=8,sticky=W)
    
    l2 = Label(f1_1,text='有效长度 Lw',font=(10))
    l2.grid(row=2,column=0,padx=20,pady=8,sticky=W)
    yx = StringVar()
    yx.set(18)
    e2 = Entry(f1_1,textvariable=yx)
    e2.grid(row=2,column=1)
    l2_2 = Label(f1_1,text='mm',font=(10))
    l2_2.grid(row=2,column=2,pady=8,sticky=W)
    
    l3 = Label(f1_1,text='滚子半径 R',font=(10))
    l3.grid(row=3,column=0,padx=20,pady=8,sticky=W)
    R = StringVar()
    R.set(16)
    e3 = Entry(f1_1,textvariable=R)
    e3.grid(row=3,column=1)
    l3_3 = Label(f1_1,text='mm',font=(10))
    l3_3.grid(row=3,column=2,pady=8,sticky=W)
    
    l6 = Label(f1_1,text='弹性模量 E',font=(10))
    l6.grid(row=6,column=0,padx=20,pady=8,sticky=W)
    E = StringVar()
    E.set(200000)
    e6 = Entry(f1_1,textvariable=E)
    e6.grid(row=6,column=1)
    l6_6 = Label(f1_1,text='Mpa',font=(10))
    l6_6.grid(row=6,column=2,pady=8,sticky=W)
    
    l7 = Label(f1_1,text='泊松比 μ',font=(10))
    l7.grid(row=7,column=0,padx=20,pady=8,sticky=W)
    mo = StringVar()
    mo.set(0.3)
    e7 = Entry(f1_1,textvariable=mo)
    e7.grid(row=7,column=1)
    
    l8 = Label(f1_1,text='滚子轴向网格数 Xs',font=(10))
    l8.grid(row=8,column=0,padx=20,pady=8,sticky=W)
    Xs = StringVar()
    Xs.set(60)
    e8 = Entry(f1_1,textvariable=Xs)
    e8.grid(row=8,column=1)
    
    l9 = Label(f1_1,text='滚子径向网格数 Ys',font=(10))
    l9.grid(row=9,column=0,padx=20,pady=8,sticky=W)
    Ys = StringVar()
    Ys.set(40)
    e9 = Entry(f1_1,textvariable=Ys)
    e9.grid(row=9,column=1)
    
    l10 = Label(f1_1,text='施加载荷 F',font=(10))
    l10.grid(row=10,column=0,padx=20,pady=8,sticky=W)
    F = StringVar()
    F.set(1000)
    e10 = Entry(f1_1,textvariable=F)
    e10.grid(row=10,column=1)
    l10_10 = Label(f1_1,text='N',font=(10))
    l10_10.grid(row=10,column=2,pady=8,sticky=W)
    
    
    b = Button(f1_1,text='开始计算',command=lambda :yzds.fun(float(cd.get()),float(R.get()),float(yx.get()),float(E.get())
                  ,float(mo.get()),int(Xs.get()),int(Ys.get()),float(F.get()),f1,canvas1,f2,canvas2),fg='red')
    b.grid(row=11,column=0,columnspan=2,padx=30,pady=5,ipadx=25,)
    
    
    
    
    f1_2 = Frame(Fr)
    f1_2.grid(row=1,column=0,sticky=N+W,padx=20)
    l9 = Label(f1_2,text='参数对应示意图',font=('黑体',15))
    l9.grid(row=0,column=0,padx=20,pady=8,sticky=W)
    c = Canvas(f1_2,bg='white',height=270,width=320)
    c.grid(row=1,column=0,padx=20,pady=40)
    img = PhotoImage(file = 'syt.gif')
    c.create_image(0,0,anchor='nw',image=img)
    
    
    
    
    #########  绘图   ###################################
    f2_1 = Frame(Fr)
    f2_1.grid(row=0,column=1,pady=20,sticky=W,padx=30)
    
    lr = Label(f2_1,text='计算结果',font=('黑体',15))
    lr.pack(anchor='w',pady=2)
# =============================================================================
#     b1 = Button(f2_1,text='绘图1',command=hui1,fg='blue')
#     b1.pack(anchor='w',ipadx=20)
# =============================================================================
    text1=StringVar()
    text1.set('图1 - 最大接触应力分布图')
    lr_1 = Label(f2_1,textvariable=text1,font=(10))
    lr_1.pack()
    
    f1 = Figure(figsize=(7, 3), dpi=100)
    canvas1 = FigureCanvasTkAgg(f1, master=f2_1)
    canvas1.show()
    canvas1.get_tk_widget().pack(pady=10,anchor='w')
    #工具按钮
    toolbar1 = NavigationToolbar2TkAgg(canvas1, f2_1)
    toolbar1.update()
    canvas1._tkcanvas.pack()
    
        
    f2_2 = Frame(Fr)
    f2_2.grid(row=1,column=1,pady=2,sticky=W,padx=30)
# =============================================================================
#     b2 = Button(f2_2,text='绘图2',command=hui2,fg='blue')
#     b2.pack(anchor='w',ipadx=20)
# =============================================================================
    text2=StringVar()
    text2.set('图2 - 滚子接触应力三维分布图')
    lr_2 = Label(f2_2,textvariable=text2,font=(10))
    lr_2.pack()
    
    f2 = Figure(figsize=(7, 3), dpi=100)
    canvas2 = FigureCanvasTkAgg(f2, master=f2_2)
    canvas2.show()
    canvas2.get_tk_widget().pack(pady=2,anchor='w')
    #工具按钮
    toolbar2 = NavigationToolbar2TkAgg(canvas2, f2_2)
    toolbar2.update()
    canvas2._tkcanvas.pack()
    #############################################
    win.mainloop()

