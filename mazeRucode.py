from sys import stdout

maze = [[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
]
 
class turtle:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.numzero = 1

	def knock(self, maze):
		if (self.x < 19 and maze[self.y][self.x + 1] == 2):
			stdout.write("R\n")
			ans = int(input())
			if (ans == 1):
				maze[self.y][self.x + 1] = 0
				self.numzero += 1
			else:
				maze[self.y][self.x + 1] = 1
		if (self.y < 19 and maze[self.y + 1][self.x] == 2):
			stdout.write("D\n")
			ans = int(input())
			if (ans == 1):
				maze[self.y + 1][self.x] = 0
				self.numzero += 1
			else:
				maze[self.y + 1][self.x] = 1
		if (self.x > 0 and maze[self.y][self.x - 1] == 2):
			stdout.write("L\n")
			ans = int(input())
			if (ans == 1):
				maze[self.y][self.x - 1] = 0
				self.numzero += 1
			else:
				maze[self.y][self.x - 1] = 1
		if (self.y > 0 and maze[self.y - 1][self.x] == 2):
			stdout.write("U\n")
			ans = int(input())
			if (ans == 1):
				maze[self.y - 1][self.x] = 0
				self.numzero += 1
			else:
				maze[self.y - 1][self.x] = 1
		maze[self.y][self.x] = 4
		self.numzero -= 1
		return maze

	def printmaze(self, maze):
		self.y = 0
		for i in maze:
				self.x = 0
				for j in i:
					if (j == 2):
						maze[self.y][self.x] = 1
					if (j == 4):
						maze[self.y][self.x] = 0
					self.x += 1
				self.y += 1
		stdout.write("!\n")
		n = 19
		for i in maze:
			for j in i:
				stdout.write("%d" % j)
			if (n > 0):
				stdout.write("\n")
				n -= 1
		stdout.flush()

	def start(self, maze):
		while (self.numzero != 0):
			self.y = 0
			for i in maze:
				self.x = 0
				for j in i:
					if (j == 0):
						maze = self.knock(maze)		
						#self.printmaze(maze)		
					self.x += 1
				self.y += 1
		return maze

tur = turtle()
maze = tur.start(maze)
tur.printmaze(maze)
