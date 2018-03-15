import sys
def SolveProblem(file):
	fo=open(file,'r')
	output = open("output",'w')
	N = int(fo.readline())
	for i in range(1,N+1):
		r,c = map(int,fo.readline().strip().split(" "))
		maze=[fo.readline().strip().split(" ") for x in range(r)]
		maps = [['' for x in range(c)] for y in range(r)]
		for x in range(r):
			for y in range(c):
				minimum = maze[x][y]
				direction = ''
				if x+1 < r and maze[x+1][y] <= minimum:
					minimum = maze[x+1][y]
					direction = 'S'
				if y+1 < c and maze[x][y+1] <= minimum:
					minimum = maze[x][y+1]
					direction = 'E'
				if y-1 >= 0 and maze[x][y-1] <= minimum:
					minimum = maze[x][y-1]
					direction = 'W'
				if x-1 >= 0 and maze[x-1][y] <= minimum:
					minimum = maze[x-1][y]
					direction = 'N'
				if minimum == maze[x][y]:
					direction = '0'
				maps[x][y] = direction
		next_label = 'a'
		for xi in range(r):
			for xj in range(c):
				(ui,uj) = (xi,xj)
				label = []
				label.append((ui,uj))
				while maps[ui][uj] != '0' and maps[ui][uj].isupper():
					if maps[ui][uj] == 'S':
						ui += 1
					elif maps[ui][uj] == 'E':
						uj += 1
					elif maps[ui][uj] == 'W':
						uj -= 1
					elif maps[ui][uj] == 'N':
						ui -= 1
					label.append((ui,uj))
				if maps[ui][uj] == '0':
					for (vi,vj) in label:
						maps[vi][vj] = next_label
					next_label=chr(ord(next_label)+1)
				else:
					for (vi,vj) in label:
						maps[vi][vj] = maps[ui][uj]
		output.write("Case #{}: \n".format(i))
		for i in range(r):
			output.write(" ".join(maps[i][j] for j in range(c))+'\n')
	fo.close()
	output.close()

if __name__ == '__main__':
	file = sys.argv[1]
	SolveProblem(file)









