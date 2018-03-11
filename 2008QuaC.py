import sys
import math
def SolveProblem(inputfile):
	fo=open(inputfile,'r')
	caseNumber = int(fo.readline())
	output = open("output",'w')
	for i in range(1,caseNumber+1):
		f,R,t,r,g = map(float,fo.readline().split())
		area = 0.0
		rad = R-t-f
		x1 = r+f
		y1 = r+f
		while x1 <= rad:
			x2 = x1+g-2*f
			x1Norm= x1/rad
			x2Norm = x2/rad
			while y1<=rad:
				y2 = y1+g-2*f
				y1Norm = y1/rad
				y2Norm = y2/rad
				area += intersection(x1Norm,y1Norm,x2Norm,y2Norm)*rad*rad
				y1 = y1+g+2*r
			x1 = x1+g+2*r
			y1 = r+f
		output.write("Case #{}: {}  \n".format(i,"{:.6f}".format(1.0-area/(math.pi*R*R/4))))
	fo.close()
	output.close()


def intersection(x1,y1,x2,y2):
	if(x1*x1+y1*y1 >= 1):
		return 0;
	if(x2*x2+y2*y2 <=1 ):
		return (x2-x1)*(y2-y1)
	EPS2= 1e-14
	if((x2-x1)*(y2-y1) <  EPS2):
		return (x2-x1)*(y2-y1)/2
	mx = (x1+x2)/2
	my = (y1+y2)/2
	return intersection(x1,y1,mx,my)+\
	intersection(mx,y1,x2,my)+\
	intersection(x1,my,mx,y2)+\
	intersection(mx,my,x2,y2)

if __name__ == '__main__':
	file = sys.argv[1]
	SolveProblem(file)

