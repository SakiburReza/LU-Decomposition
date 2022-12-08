"""
Created on Thu Jul 11 12:53:39 2019

@author: Sakibur Reza
"""

import numpy as np
import matplotlib.pyplot as plt

def LU_Decomposition(matrix,n):
    
    L_matrix=[[0 for x in range(n)]  
                for y in range(n)]
    U_matrix=[[0 for x in range(n)]  
                for y in range(n)]
    
    #L_matrix=np.zeros([n,n])
    #U_matrix=np.zeros([n,1])
 
    check=0
    for i in range(n): 
        k=i
        while k<n:
            sum = 0
            j=0
            while j<i:
                sum += (L_matrix[i][j] * U_matrix[j][k]) 
                j+=1
            U_matrix[i][k] = matrix[i][k] - sum
            k+=1
        
        k=i   
        while k<n:
            if not (i != k): 
                L_matrix[i][i] = 1
                k+=1
            else: 
                sum = 0 
                j=0
                while j<i:
                    sum += (L_matrix[k][j] * U_matrix[j][i])
                    j+=1
                L_matrix[k][i] = (matrix[k][i] - sum) /U_matrix[i][i]
                k+=1
        count=0
        for j in range(n):
            if U_matrix[i][j] ==0 :
                count=count+1
            if count==n:
                check=1
             
    return L_matrix, U_matrix,check
file = open("in1.txt","r")
file2=open("out1.txt","w")
lines=file.readlines()

n=int(lines[0])
print(n);
A=np.zeros([n,n])
B=np.zeros([n,1])
for i in range(n):
    for j in range(n):
        temp=lines[i+1].split(" ")
        A[i][j]=float(temp[j])
for i in range(n):
        B[i]=float(lines[i+1+n])
print(A)
print(B)
L_Matrix, U_Matrix,m= LU_Decomposition(A,n)
L_Matrix=np.matrix(L_Matrix)
U_Matrix=np.matrix(U_Matrix)
if m==1:
    print("No unique solution")
print(L_Matrix)
print(U_Matrix)
Y_Matrix=np.dot(np.linalg.inv(L_Matrix),B)
X_Matrix=np.dot(np.linalg.inv(U_Matrix),Y_Matrix)

#print("{0:.2f}".format(Y_Matrix))
#print('%.2f'%X_Matrix)
s1=""
s2=""
s3=""
s4=""
s5=""
for i in range(n):
    for j in range (n):
        s1=s1+str(('%.4f'%L_Matrix[i,j]))+" "
    s1=s1+"\n"
s1=s1+"\n"
print(s1)
for i in range(n):
    for j in range (n):
        s2=s2+str(('%.4f'%U_Matrix[i,j]))+" "
    s2=s2+"\n"
s2=s2+"\n"
print(s2)
if m==1:
    s3="No unique solution\n"
    file2.write(s1+s2+s3)
else:
    for i in range (n):
        for j in range (1):
            s4=s4+str('%.4f'%Y_Matrix[i,j])+"\n"
    s4=s4+"\n"
    print(s4)
    for i in range (n):
        for j in range(1):
            s5=s5+str('%.4f'%X_Matrix[i,j])+"\n"
    print(s5)
file2.write(s1+s2+s3+s4+s5)
file.close()
file2.close()



    