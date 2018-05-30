# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 18:49:38 2018

@author: dell
"""

from tkinter import *
import qjbl 
qjbl.bl()

def main2(x):

    def fun1():
        import main3x1
        tl = Toplevel()
        tl.title('圆锥滚子直线型')
        main3x1.func1(x,tl)
    def fun2():
        import main3x2
        tl = Toplevel()
        tl.title('圆锥滚子圆弧型')
        main3x2.func2(x,tl)
    def fun3():
        import main3x3
        tl = Toplevel()
        tl.title('圆锥滚子对数型')
        main3x3.func3(x,tl)
        
############################################        
        
    def fun4():
        import main3x4
        tl = Toplevel()
        tl.title('圆柱滚子直线型')
        main3x4.func4(x,tl)
    def fun5():
        import main3x5
        tl = Toplevel()
        tl.title('圆柱滚子圆弧型')
        main3x5.func5(x,tl)
    def fun6():
        import main3x6
        tl = Toplevel()
        tl.title('圆柱滚子对数型')
        main3x6.func6(x,tl)

    
    f1 = Frame(x)
    f1.pack()
    
    l1 = Label(f1,text='圆柱滚子',font=('黑体',40))
    l1.grid(row=0,column=0,pady=50,padx=100)



    b1=Button(f1,text = '直线型',font=('黑体',20),
                command=fun4,).grid(row=1,column=0,pady=15)
    Button(f1,text = '圆弧型',font=('黑体',20),
                command=fun5,).grid(row=2,column=0,pady=15)
    Button(f1,text = '对数型',font=('黑体',20),
                command=fun6,).grid(row=3,column=0,pady=15)
    
    Label(f1,text='').grid(row=4,column=0,pady=20)
    
    
    
    ###################################
    
    
    l2 = Label(f1,text='圆锥滚子',font=('黑体',40))
    l2.grid(row=0,column=1,pady=50,padx=100)



    Button(f1,text = '直线型',font=('黑体',20),
                command=fun1).grid(row=1,column=1,pady=15)
    Button(f1,text = '圆弧型',font=('黑体',20),
                command=fun2).grid(row=2,column=1,pady=15)
    Button(f1,text = '对数型',font=('黑体',20),
                command=fun3).grid(row=3,column=1,pady=15)
    Label(f1,text='').grid(row=4,column=1,pady=20)
    
    x.mainloop()


