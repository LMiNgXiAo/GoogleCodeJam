import sys
inputfile = sys.argv[1]
fo = open(inputfile, "r")
output = open("ouputfile", "w")
case_number = int(fo.readline())
serves={}
for i in range(1, case_number + 1):
	switch_number = 0
	flag = True
	serve_number = int(fo.readline())
	t = serve_number
	for j in range(serve_number):
		serves[fo.readline()] = flag
	quires_number = int(fo.readline())
	for k in range(quires_number):
		quire = fo.readline()
		if(t > 1 and serves[quire] == flag):
			t -= 1
			serves[quire] = not flag
		if(t==1):
			if(serves[quire]== flag):
				switch_number += 1
				flag = not flag
				t = serve_number-1
	output.write("Case #{}: {}".format(i,switch_number))
	output.write("\n")
fo.close()
output.close()
