import numpy as np
from matplotlib import pyplot as plt
def dft1(x,N):
	X=[]
	for k in np.arange(0,N//2):
		s=0
		for n in np.arange(0,N//2):
			l=k/N
			s=s+x[2*n]*np.exp(-1j*2*np.pi*2*n*l)
		X.append(s)
	return X
def dft2(x,N):
	X=[]
	for k in np.arange(0,N//2):
		s=0
		for n in np.arange(0,N//2):
			l=k/N
			s=s+x[(2*n)+1]*np.exp(-1j*2*np.pi*((2*n)+1)*l)
		X.append(s)
	return X
a=[1,2,3,4,5,6,7,8]
N=len(a)
X1=np.array(dft1(a,N))
X2=np.array(dft2(a,N))
X=X1+X2# 0 to N/2-1
G=X1-X2# N/2 to N-1
print(X)
print()
print(G)
