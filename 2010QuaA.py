import sys
def SolveProblem(file):
	fo = open(file,'r')
	output = open('output','w')
	T = int(fo.readline())
	for i in range(1,T+1):
		state=''
		flag = True
		N,K =map(int,fo.readline().strip().split(' '))
		dic={}
		for j in range(1,N+1):
			dic[j] = 0
		dic[0] = 1
		for x in range(K):
			for l in range(N,0,-1):
				flag2 = True
				for k in range(0,l):
					if dic[k] == 0:
						flag2=False
						break
				if flag2 == True:
					if dic[l] == 0:
						dic[l] = 1
					else:
						dic[l] = 0
		for element in dic.values():
			if element == 0:
				flag = False
				break
		if flag == True:
			state = 'ON'
		else:
			state = 'OFF'
		output.write("Case #{}: {} \n".format(i,state))
		print("Case {} done! \n".format(i))
	fo.close()
	output.close()

if __name__ == '__main__':
	file = sys.argv[1]
	SolveProblem(file)
