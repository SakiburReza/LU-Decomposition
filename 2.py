# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 12:02:09 2019

@author: Lenovo
"""

import numpy as np
def printf(tableu,row,column):
    for i in range(row):
        for j in range(column):
            
            print('%8.2f'%tableu[i][j],end="")
        print("\n")
    print("\n")
    print("\n")
def algorithm(tableu,row,column,n):
    
    piv_row_val=9999999
   
    piv_col_index=list(tableu[0]).index(min(list(tableu[0])))
    #print(piv_col_index)
    for i in range (1,row):
        tableu[i][column-1]=tableu[i][column-2]/tableu[i][piv_col_index]
        if tableu[i][column-1]<piv_row_val:
            piv_row_val=tableu[i][column-1]
            piv_row_index=i
    printf(tableu,row,column)
    #print(piv_row_index)
    
    for i in range(1,column-1):
        tableu[piv_row_index][i]=tableu[piv_row_index][i]/tableu[piv_row_index][piv_col_index]
    for i in range(row):
        if i==piv_row_index:
            print("X:",piv_col_index,"=",tableu[i][column-2])
            continue
        else:

            tableu[i] = tableu[i] - tableu[piv_row_index]*tableu[i][piv_col_index]
    printf(tableu,row,column)
    for i in range(1,column-1):
        if tableu[0][i]<0:
            toggle=1
            break
        
    toggle=0    
    if toggle==1:
        algorithm(tableu,row,column,n)
    else:
        
        print("Max Value:",tableu[0][column-2])
        
        
    
        
  
    
    
file=open("in2.txt","r")
lines=file.readlines()
num_lines=sum(1 for line in file)
#print(lines)
s=lines[0].split(" ")
#print(len(s)+1)
n=len(s)
file.seek(0)

#print(num_lines)
row=num_lines
column=num_lines+len(s)+2
tableu=np.zeros([row,column])


for i in range(row):
    for j in range(n+1):
        if i==0 and j==0:
            tableu[i][j]=1
        elif i==0 and j!=0:
            tableu[i][j]=-float((lines[i].split(" ")[j-1]))
        elif j!=0:
            tableu[i][j]=float((lines[i].split(" ")[j-1]))
for i in range(1,row):
    for j in range(n,column-1):
        if i+n==j:
            tableu[i][j]=1
for i in range(1,row):
    tableu[i][column-2]=(float(lines[i].split(" ")[n]))

printf(tableu,row,column)
algorithm(tableu,row,column,n)











