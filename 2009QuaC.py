import sys
def SolveProblem(file):
	fo = open(file,'r')
	output = open('output','w')
	N = int(fo.readline())
	words = 'welcome to code jam'
	for i in range(1,N+1):
		s=fo.readline()
		n = count(s,words)%10000
		output.write(" Case #{}: {:0=4} \n".format(i,n))

def count(s,words):
	dp={}
	if s[0] == words[0]:
		dp[0,0] = 1
	else:
		dp[0,0] = 0
	for i in range(1,len(s)):
		if s[i] == words[0]:
			dp[i,0] = dp[i-1,0]+1
		else:
			dp[i,0] = dp[i-1,0]

		for j in range(1,len(words)):
			if j>i-1:
				dp[i-1,j]=0;
			if s[i] == words[j]:
				dp[i,j] = dp[i-1,j]+dp[i-1,j-1]
			else:
				dp[i,j] = dp[i-1,j]
	print(dp)
	return dp[len(s)-1,len(words)-1]
if __name__ == '__main__':
	file = sys.argv[1]
	SolveProblem(file)


