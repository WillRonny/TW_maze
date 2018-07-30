# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 09:08:55 2018

@author: Will
"""
#%%
#输入转为Int

import numpy as np 

roderace=input("roderace=")
edge = []
def input_trans(roderace): 
    global data
    A = roderace.split(';')
    new_roderace = []
    for item in A:
        for i in item.split(' '):
            new_roderace.append(i.split(','))
    data = np.array(new_roderace).astype(int)
    #坐标转换
    for i in data :
        i[0]=2*i[0]+1
        i[1]=2*i[1]+1
    #找到左边之间的相通的边    
    global edge
    for j in range(0,len(data),2):
       x= (data[j][0]+data[j+1][0])/2
       y= (data[j][1]+data[j+1][1])/2
       edge.append([int(x),int(y)])
    return data,edge

       
  
#[item.split(' ') for item in A]        
        
maze=[]
print('请输入尺寸：')
while True:
    temp = input()
    #输入多行 加上下面两行
#    if temp == '':
#        break
    maze.append([int(i) for i in temp.split(' ')]) 
row,col = maze[0][0],maze[0][1]


def genmaze(row,col):
    maze_trans = np.zeros((2*row+1,2*col+1))
    #添加点
    for pos in edge:
        maze_trans[pos[0],pos[1]]=1
    for pos in data:
        maze_trans[pos[0],pos[1]]=1
    return maze_trans
C = genmaze(row,col)

MAZE = []
for item in C:
    for j in item:
        if j == 0:
            MAZE.append(['w'])
        MAZE.append(['R'])



    