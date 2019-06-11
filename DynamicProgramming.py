import numpy as np
global M

M = [[4,7,1,6], [5,7,3,9], [3,2,1,2], [7,1,6,3]]

def path(m, n, cost):	
	global W
	global M
	print('m, n: ', m, n)
	print('cost: ', cost)
	if m ==0 and n == 0:
		if M[m][n] == cost:
			# W[m][n] = 1
			return 1
		else:
			# W[m][n] = 0
			return 0
	elif W[m][n] != 0:
		# print('llega aca')
		# print('m, n: ', m, n)
		# print('W[m][n]: ', W[m][n])
		# print('--------------------------')
		return W[m][n]
	else:
		if m == 0:
			W[m][n] = path(m, n-1, cost - M[m][n])
			return W[m][n]
		elif n == 0:
			W[m][n] = path(m-1, n, cost - M[m][n])
			return W[m][n]
		else:
			W[m][n] = path(m-1, n, cost - M[m][n]) + path(m, n-1, cost - M[m][n])
			return W[m][n]


global W

W = np.zeros((4, 4)) 
print('M')
print(M[0][0])
print(path(4-1, 4-1, 25))
print('W')
print(W)
