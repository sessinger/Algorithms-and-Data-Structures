import numpy as np

def OH(D,indices):
    ZZ = np.empty((D.shape[0],1))
    for feat in range(D.shape[1]):
		x = D[:,feat]
		u = set(x)
		Z = np.zeros((len(x),len(u)))
		for i in range(len(x)):
			ind = list(u).index(x[i])
			Z[i,ind]=1
		ZZ = np.append(ZZ,Z,axis=1)
    return ZZ[:,1:]
	
if __name__ == "__main__":
	x = ['one','two','one','one','two','three','four']
	y = ['jack','be','nimble','jack','be','jack','jack']
	D = np.vstack((x,y)).T
	D_out = OH(D)
	print D_out
