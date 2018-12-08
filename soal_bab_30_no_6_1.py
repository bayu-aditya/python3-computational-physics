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
T1 = 20.2689524008   # T_1,1 saat detik ke 5
T2 = 29.0862937856   # T_1,2 saat detik ke 5
T3 = 47.5714047169   # T_1,3 saat detik ke 5
T4 = 1.57654819193   # T_2,1 saat detik ke 5
T5 = 6.92925971783   # T_2,2 saat detik ke 5
T6 = 28.879000508    # T_2,3 saat detik ke 5
T7 = 17.1535516993   # T_3,1 saat detik ke 5
T8 = 25.3934547743   # T_3,2 saat detik ke 5
T9 = 44.4560040154   # T_3,3 saat detik ke 5
a = 2*(1-lam)
var = ('1,1','1,2','1,3','2,1','2,2','2,3','3,1','3,2','3,3')

# Ax = B
# Matriks A
for i in range(0,m+1):
	for j in range(0,m+1):
		if (i == j):
			A[i, j] = 2*(1+lam)			# nilai diagonal
			if ((j-3) >= 0):
				A[i, j - 3] = - lam	# diagonal kiri
			if ((j+3) <= m):
				A[i, j + 3] = - lam 	# diagonal kanan
print("Matriks A adalah \n",A,"\n")

# Matriks B
B[0] = 60*lam + a*T1 + lam*T2
B[1] = 60*lam + a*T2 + lam*T1 + lam*T3
B[2] = 180*lam + a*T3 + lam*T2
B[3] = a*T4 + lam*T5
B[4] = a*T5 + lam*T4 + lam*T6
B[5] = 120*lam + a*T6 + lam*T5
B[6] = 50*lam + a*T7 + lam*T8
B[7] = 50*lam + a*T8 + lam*T7 + lam*T9
B[8] = 170*lam + a*T9 + lam*T8

print("Matriks B adalah \n",B,"\n")

C = gaussPivot(A,B)
for i in range(0,9):
    print("nilai dari T_",var[i]," saat detik ke 10 adalah ",C[i])