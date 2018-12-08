"""----------------------------------------------------------------------
									BAB 30 NOMOR 6
							Bayu Aditya - 1606922390
----------------------------------------------------------------------"""
import numpy as np
from bayu_algebra import gaussPivot

# inisialisasi data
n = 9								# banyaknya persamaan
m = n - 1							# definisi variabel m
k = 0.835
delt = 10
delx = 10
lam = k*delt / delx			# definisi lamda
A = np.zeros([n,n])			# membuat matriks n x n
B = np.zeros([n])				# membuat vektor ukuran n
var = ('1,1','1,2','1,3','2,1','2,2','2,3','3,1','3,2','3,3')

# Ax = B
# Matriks A
for i in range(0,m+1):
	for j in range(0,m+1):
		if (i == j):
			A[i, j] = 2*(1+lam)			# nilai diagonal
			if (j >= 1):
				if (i % 3 != 0):
					A[i, j - 1] = - lam	# diagonal kiri
			if (j <= m - 1):
				if ((i+1) % 3 != 0):
					A[i, j + 1] = - lam 	# diagonal kanan
print("Matriks A adalah \n",A,"\n")

# Matriks B
B[0] = 60*lam ; B[1] = 60*lam ; B[2] = (60+120)*lam
B[3] = 0 ; B[4] = 0 ; B[5] = 120*lam
B[6] = 50*lam ; B[7] = 50*lam ; B[8] = (50+120)*lam
print("Matriks B adalah \n",B,"\n")

C = gaussPivot(A,B)
for i in range(0,9):
    print("nilai dari T_",var[i]," saat detik ke 5 adalah ",C[i])