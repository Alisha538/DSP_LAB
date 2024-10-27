import numpy as np
def fft(x):

		N=len(x)

		xe=x[0::2]
		xo=x[1::2]
		Wn1=[]
		Wn=np.exp(-1j*2*np.pi*(np.arange(0,N//2))/N)
		Xe2=np.array(np.fft.fft(xe))
		Xo2=np.array(np.fft.fft(xo))
		Xe=Xe2
		Xo=Xo2*Wn
		X=Xe+Xo
		Y=Xe-Xo
		return X,Y
x=[1,-1,2,4]
X,Y=fft(x)
X1=list(X)
Y1=list(Y)
Z=X1+Y1
print(Z)
