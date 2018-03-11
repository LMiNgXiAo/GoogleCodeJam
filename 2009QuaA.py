import sys
def SolveProblem(file):
	fo = open(file,'r')
	output = open("output",'w')
	L,D,N = map(int,fo.readline().split())
	dic=[fo.readline().strip("\n") for x in range(D)]
	for i in range(1,N+1):
		num = 0
		patterns = fo.readline().strip("\n")
		lists = [([0]*26) for i in range(L)]
		j=0
		h=0
		while h < len(patterns):
			if patterns[h] == "(":
				h += 1
				while patterns[h] != ")":
					lists[j][ord(patterns[h])-97] = 1
					h += 1
			else:
				lists[j][ord(patterns[h])-97] = 1
			j += 1
			h += 1
		for word in dic:
			k=0
			for b in word:
				if lists[k][ord(b)-97] == 1:
					k += 1
				else:
					break
			if k== L:
				num += 1
		output.write("Case #{}: {} \n".format(i,num))
	output.close()
	fo.close()

if __name__ == '__main__':
	file = sys.argv[1]
	SolveProblem(file)


