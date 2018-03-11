import sys
import heapq
def loadinputfile(inputfile):
	fo = open(inputfile,'r')
	output = open("output2",'w')
	caseNumber = int(fo.readline())
	for i in range(1,caseNumber+1):
		trips=[]
		turnaroundTime = int(fo.readline())
		number = fo.readline().split()
		na, nb = int(number[0]), int(number[1])
		for a in range(na):
			tmp=fo.readline().split()
			leave = int(tmp[0].split(":")[0])*60+int(tmp[0].split(":")[1])
			arrive = int(tmp[1].split(":")[0])*60+int(tmp[1].split(":")[1])
			trips.append([leave,arrive,0])
		for b in range(nb):
			tmp = fo.readline().split()
			leave = int(tmp[0].split(":")[0])*60+int(tmp[0].split(":")[1])
			arrive = int(tmp[1].split(":")[0])*60+int(tmp[1].split(":")[1])
			trips.append([leave,arrive,1])
		trips.sort()
		trainNumber=[0,0]
		trains=[[],[]]
		for trip in trips:
			d=trip[2]
			if trains[d] and trains[d][0] <= trip[0]:
				heapq.heappop(trains[d])
			else:
				trainNumber[d] += 1
			heapq.heappush(trains[1-d],trip[1]+turnaroundTime)
		output.write("Case #{}: {} {}  \n".format(i,trainNumber[0],trainNumber[1]))


if __name__ == "__main__":
	file = sys.argv[1]
	loadinputfile(file)
