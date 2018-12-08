"""-----------------------------------------------------------------------
									BAB 27 NOMOR 4
							Bayu Aditya - 1606922390
-----------------------------------------------------------------------"""
import matplotlib.pyplot as plt
import numpy as np
from bayu_algebra import gaussPivot

n = 9
h = 20/(n+1)
x = np.arange(0,20+h,h)

# Matriks A
A = np.zeros([n,n])
for i in range(0,n):
    for j in range(0,n):
        if (i == j):
            A[i,j] = -14. - h**2    # NIlai elemen diagonal
            if ((j-1) >= 0):
                A[i,j-1] = 7 + h    # Nilai elemen diagonal kiri
            if ((j+1) <= n-1):
                A[i,j+1] = 7 - h    # Nilai elemen diagonal kanan
print("Matriks A adalah \n",A,"\n")

# Matriks B
B = []
for i in range(0,n):
    B.append(-x[i+1]*h**2)
B[0] = -x[1]*h**2 - 5*(7+h)         # mengganti baris awal matriks B
B[n-1] = -x[n]*h**2 - 8*(7-h)       # mengganti baris terakhir matriks B
print("Matriks B adalah \n",B,"\n")

# Matriks C
C = gaussPivot(A,B)
for i in range(1,n+1):
    print("nilai dari y_{:d} adalah {:7.6f}".format(i,C[i-1]))

C.insert(0,5.)   ; C.append(8.)
plt.plot(x,C)   ;plt.title("Grafik Soal 27.4")
plt.xlabel('Waktu (sec)')   ; plt.ylabel('$y(x)$')
plt.grid(True) ; plt.show()