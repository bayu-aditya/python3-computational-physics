"""-----------------------------------------------------------------------
									BAB 29 NOMOR 8
							Bayu Aditya - 1606922390
-----------------------------------------------------------------------"""
import numpy as np
from bayu_algebra import gaussPivot

# input data
m = 4
n = m**2
A = np.zeros([n,n])
B = np.zeros([n])
var = ('0,0','1,0','2,0','3,0','0,1','1,1','2,1','3,1','0,2','1,2','2,2','3,2','0,3','1,3','2,3','3,3')

# Matriks A
A[0,0] = -2.
for i in range(0,n):
	for j in range(0,n):
		if (i ==j):
			if (i>=m):
				if (i%4 !=0):
					A[i,j] = -4.
				else:
					A[i,j] = -3.
			elif (i>0 and i<m):
				A[i,j] = -3.
			if ((j+1)<=(n-1)):
				if ((i+1)%m != 0):
					A[i, j+1] = 1.
			if ((j-1)>=(0)):
				if (i%m !=0):
					A[i, j-1] = 1.
			if ((j+m)<=(n-1)):
				A[i, j+m] = 1.
			if ((j-m)>=0):
				A[i, j-m] = 1.
print("Matriks A adalah :\n",A,"\n")

# Matriks B
B[3] = 0        ;B[7] = -25.    ;B[11] = -50.   ;B[12] = 0
B[13] = -25     ;B[14] = -50.   ;B[15] = -75.-75
print("Matriks B adalah :\n",B,"\n")

C = gaussPivot(A,B)
for i in range(0,n):
    print("Nilai dari T_",var[i]," adalah ",C[i]," celcius")