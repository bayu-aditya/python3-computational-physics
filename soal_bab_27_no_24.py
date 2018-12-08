"""-----------------------------------------------------------------------
									BAB 27 NOMOR 24
							Bayu Aditya - 1606922390
-----------------------------------------------------------------------"""
import numpy as np
from bayu_algebra import gaussPivot
import matplotlib.pyplot as plt

# pendefinisian data
r = np.linspace(0, 0.9, 10)         # membuat r0 sampai r9
n = len(r)                          # ukuran matriks n = 10
h = (r[1] - r[0])                   # definisi nilai h
lam = h / 2.0                       # definisi nilai lamda
a = 1 - (lam / 0.1)                 # nilai untuk diagonal kiri
b = 1 + (lam / 0.1)                 # nilai untuk diagonal kanan
A = np.zeros([n, n])
B = np.zeros([n])

# Ax = B
# Matriks A
for i in range(0, n):
	for j in range(0, n):                      # loop dari 0 sampai 9
		if (i == j):
			A[i, j] = -2	                        # nilai diagonal
			if ((j-1) >= 0):                        # kondisi agar tidak melebihi ukuran matriks
				A[i, j - 1] = 1 - (lam / r[i])   # nilai diagonal kiri
			if ((j+1) <= n-1):
				A[i, j + 1] = 1 + (lam / r[i])   # nilai diagonal kanan
A[0,0] = -3 ; A[0,1] = 4 ; A[0,2] = -1	     # definisi titik awal
print("Matriks A adalah \n", A,"\n")

# Matriks B
s = float(input("masukkan nilai S : "))         # input nilai s
for i in range(1, n - 1):                       # loop dari 1 sampai 8
	B[i] = -s * h**2
B[n - 1] = -s * h**2 - (1 + lam/r[n-1])         # nilai untuk baris terakhir
#print("Matriks B adalah \n",B)

C = gaussPivot(A,B)
for i in range(0,n):
    print("Nilai dari T_{:d} adalah {:7.6f}".format(i,C[i]))
plt.title('Grafik Soal 27.24')
plt.xlabel("Jari-jari (r)") ; plt.ylabel("T(r)")
plt.plot(r,C)   ; plt.show()