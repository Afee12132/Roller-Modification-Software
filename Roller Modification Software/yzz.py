# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 17:50:08 2017

@author: ddell
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:08:00 2016

@author: Administrator
"""
import qjbl
import numpy as np
from matplotlib import cm
#def f1(x, y):
#    return x + np.sqrt(x**2 + y**2)


#def a_ij(i,j,k,l):
#    return (j-l+0.5) * np.log(f1(j-l+0.5, i-k+0.5)/f1(j-l-0.5,i-k+0.5)) + \
#           (i-k-0.5) * np.log(f1(i-k-0.5, j-l-0.5)/f1(i-k+0.5,j-l-0.5)) + \
#           (j-l-0.5) * np.log(f1(j-l-0.5, i-k-0.5)/f1(j-l+0.5,i-k-0.5)) + \
#           (i-k+0.5) * np.log(f1(i-k+0.5, j-l+0.5)/f1(i-k-0.5,j-l+0.5))
def fun(cd,Rb,yx,E,mo,Xs,Ys,F,ff1,canvas1,ff2,canvas2):
    def a_ij(x,y,b,a):
    
        f1 = lambda x, y: x + np.sqrt(x**2 + y**2)
    
        return (x+b) * np.log(f1(y+a,x+b)/f1(y-a,x+b)) + \
               (y+a) * np.log(f1(x+b,y+a)/f1(x-b,y+a)) + \
               (x-b) * np.log(f1(y-a,x-b)/f1(y+a,x-b)) + \
               (y-a) * np.log(f1(x-b,y-a)/f1(x+b,y-a))
    
    #材料1
    E_1 = E   # MPa
    mu_1 = mo
    
    #材料2
    E_2 = E# MPa
    mu_2 = mo
    
    k = ( (1 - mu_1**2)/E_1 + (1 - mu_2**2)/E_2) / np.pi
    
    # x的界限
    x1 = -(cd/2)
    x2 = cd/2
    
    x_yx = yx/2
    
    y1 = -1
    y2 = 1
    
    # x方向网格数
    x_grid_number = Xs
    # y方向网格数
    y_grid_number = Ys
    # 网格大小
    x_grid_size = (x2 - x1) / (2 * x_grid_number)   # nuit:mm
    y_grid_size = (y2 - y1) / (2 * y_grid_number)  # nuit:mm
    
    def influence_coefficient_matrix(x_number, y_number, x_size, y_size):
        Matrix_mother = np.zeros([2 * x_number - 1, 2 * y_number - 1])
        for i in range(2 * x_number - 1):
            for j in range(2 * y_number - 1):
                Matrix_mother[i, j] = a_ij(np.abs(i - x_number+1) * 2 * x_size, np.abs(j - y_number+1) * 2 * y_size, x_size, y_size)
    
        n = 0
        P = np.zeros([x_number*y_number, x_number * y_number])
        for i in range(x_number):
            for j in range(y_number):
                t1 = Matrix_mother[(x_number-1-i):(x_number-1-i+x_number),(y_number-1-j):(y_number-1-j+y_number)]
                P[n,:] = t1.reshape(1,-1)
                n = n + 1
    
        return P
    
    P = influence_coefficient_matrix(x_grid_number, y_grid_number, x_grid_size, y_grid_size)
    
    
    ###
    
    # 圆柱的表面坐标
    R = Rb # nuit:mm3
    
    
    xa = [x1 +  (2*i + 1)* x_grid_size for i in range(x_grid_number)]
    ya = [y1 +  (2*i + 1)* y_grid_size for i in range(y_grid_number)]
    
    #xx, yy = np.meshgrid(xa, ya)#, sparse=True)
    
    #==============================================================================
    # def yuanjiao(x_n, r):
    #     a = np.arccos(x_n/r)
    #     R_r = 5 - r + r * np.sin(a)
    #     return R_r
    #==============================================================================
    
    z = np.zeros([x_grid_number, y_grid_number])
    for i in range(x_grid_number):
        for j in range(y_grid_number):
            if np.logical_and(np.logical_and(xa[i] < x_yx , xa[i] > -x_yx), np.logical_and(ya[j]<1, ya[j] > -1)):
                z[i,j] = np.sqrt(R**2 - ya[j]**2)
            
    
    
    shape = z
    #shape= np.zeros_like(z)
    #shape = np.zeros([x_grid_number, y_grid_number])
    #positon = np.logical_and(np.logical_and(xx < 1, xx > -1), np.logical_and(yy<1.5, yy > -1.5))
    #shape[positon] = z[positon]
    
    n = 0
    F_ext = F
    d_test = 0.003
    # 确定位移下限
    
    while True:
        alpha = shape - R + d_test
        b = alpha.reshape(1,-1)
        # plt.plot(b[0,:])
        for i in range(b.size):
            if b[0,i] < 0:
                b[0,i] = 0
        c = np.linalg.solve(P,b.T/k)
    
        F_calculate = 0
        for i in range(c.shape[0]):
            if(c[i,0]>0):
                F_calculate += c[i,0] * 4 * x_grid_size * y_grid_size
    
        #print(F_calculate)
    
        if(F_ext < F_calculate):
            d_test = 0.5 * d_test
        else:
            break
    d_low = d_test
    
    # 确定位移上限
    d_test = 0.1
    while True:
        alpha = shape - R + d_test
        b = alpha.reshape(1,-1)
        b[b<0] = 0
        # plt.plot(b[0,:])
    
        c = np.linalg.solve(P, b.T/k)
    
        c[c<0] = 0
    
        F_calculate = (c * 4 * x_grid_size * y_grid_size).sum()
    
        #print(F_calculate)
    
        if(F_ext > F_calculate):
            d_test = 2 * d_test
        else:
            break
    
    d_up = d_test
    
    d_test = 0.5 * (d_up + d_low)
    
    while np.abs(d_up - d_low) > 1e-8:
    
        alpha = shape - R + d_test
        b = alpha.reshape(1,-1)
        b[b<0] = 0
        # plt.plot(b[0,:])
    
        c = np.linalg.solve(P, b.T/k)
    
        c[c<0] = 0
    
        F_calculate = (c * 4 * x_grid_size * y_grid_size).sum()
    
        #print(F_calculate)
    
    
        if(F_ext > F_calculate):
            d_low = d_test
            d_test = 0.5 * (d_up + d_low)
    
        else:
            d_up = d_test
            d_test = 0.5 * (d_up + d_low)
    
        #print(d_low,d_up)
    
    
        n = n+1
        if(n>20000):
            break
    
    
    #
    #d.max()
    #
    #a1 = (1 - mu_1**2)/E_1
    #a2 = (1 - mu_2**2)/E_2
    #
    #np.sqrt(6 * F_ext * (1/(a1+a2))**2)/np.pi
    
    Hz_s1 = 0.388 * (F_ext * (2*E_1*E_2/(E_1 + E_2))**2 / R**2)**(1/3)
    
    #0.388 * (10000 * (2*E_1*E_2/(E_1 + E_2))**2)**(1/3)
    #
    #0.388 * (10000 * E_1**2)**(1/3)
    #1.231 * (10000**2 / E_1**2)**(1/3)
    #d_test
    Hz_d1 = 1.231 * (F_ext**2 / E_1**2/R)**(1/3)
    
    #print('赫兹接触应力 = %0.3f, \t 计算接触应力 = %0.3f ' % (Hz_s1, c.max()))
    #print('赫兹接触深度 = %0.3f, \t 计算接触深度 = %0.3f ' % (Hz_d1, d_test))
    #print('赫兹接触半径 = %0.3f' % r1)
    
    
    
    qjbl.set_v('Da',c.reshape(x_grid_number, y_grid_number))
    ###图1
    ff1.clf()
    a1 = ff1.add_subplot(111)
    s1 = qjbl.get_v('Da')[:,int((y_grid_number+1)/2)]
    a1.plot(s1)
    canvas1.show()
    #text1.set('图1 - 最大接触应力分布图'+'  F='+F_ext+'N')
    
    ###图2
    ff2.clf()
    a2 = ff2.gca(projection='3d')
    x = np.arange(0, x_grid_number)
    y = np.arange(0, y_grid_number)
    X, Y = np.meshgrid(x, y)
    Z = qjbl.get_v('Da').T
    # Plot the surface.
    surf = a2.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                         linewidth=0,)
    ff2.colorbar(surf, shrink=0.5, aspect=10)
    canvas2.show()
    #text2.set('图2 - 滚子接触应力三维分布图'+'  F='+F_ext+'N')
# =============================================================================
#     import matplotlib.pyplot as plt
#     from matplotlib import cm
#     from mpl_toolkits.mplot3d import Axes3D
# =============================================================================
    
    #h = plt.contourf(ya,xa,c.reshape(x_grid_number, y_grid_number))
    #h = plt.contourf(xa,ya,1000*c.reshape(x_grid_number, y_grid_number).T)
    
    #X = np.arange(0, x_grid_number)
    #Y = np.arange(0, y_grid_number)
    #X, Y = np.meshgrid(X, Y)
    #
    #fig = plt.figure()
    #ax = fig.gca(projection='3d')
    ##
    #surf = ax.plot_surface(xa, ya, d, rstride=1, cstride=1, cmap=cm.coolwarm,
    #                       linewidth=0, antialiased=False)
    #
    #plt.show()

