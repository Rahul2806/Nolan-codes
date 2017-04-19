from __future__ import print_function
import random 
import numpy as np
from numpy.linalg import inv
import math

my_file = open("data.txt", "r+")
list = []
X=[]
Y=[]
X1=[]
Y1=[]
W = []
eta = 10^20

for i in range(6497):
	list.append(map(float,my_file.readline().strip().split('\t')))	
	X.append(list[i][0:11])
	Y.append(list[i][12:13])

w0 = random.random()
w1 = random.random()
w2 = random.random()
w3 = random.random()
w4 = random.random()	
w5 = random.random()
w6 = random.random()
w7 = random.random()
w8 = random.random()
w9 = random.random()
w10 = random.random()
W = [w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10]
W1 = np.array(W[0:11])

print("Enter the value of N :")
N = int(raw_input(),10)



for i in range(200):
	E = [0,0,0,0,0,0,0,0,0,0,0]
	E = np.matrix(E)
	for j in range(N):
		#print(E)
		X1 = np.matrix(X[j])
		Y1 = np.matrix(Y[j])
		XT = X1.transpose()
		R = np.dot(W1,XT)
		E = E + (np.dot(Y1,X1))/(1 + math.exp(np.dot(Y1,R)))
	E = -E/N
	print(E)
	W1 = W1 - eta*E
	print(W1)

#----------------------------------------------------------------------------------------------------------------------------------
Ein = 0
for i in range(N):
	
	X2 = np.matrix(X[i])
	Y2 = np.matrix(Y[i])
	XT2 = X2.transpose()
	A = math.exp(-np.dot(Y2,np.dot(W1,XT2)))
	Ein = Ein + math.log(1 + A)

Ein = Ein/N
print(Ein)
#-------------------------------------------------------------------------------------------------------------------------------------

Eout = 0
for i in range(4501,6497):
	X2 = np.matrix(X[i])
	Y2 = np.matrix(Y[i])
	XT2 = X2.transpose()
	A = math.exp(-np.dot(Y2,np.dot(W1,XT2)))
	Eout = Eout + math.log(1 + A)

Eout = Eout/N
print(Eout)
#---------------------------------------------------------------------------------------------------------
