# console based  John Conway Game o' life thing using ' ' and '#' ie '
from random import randint

class LifeSpace(object):

	def __init__(self, horizontal_size, vertical_size):
		self.horizontal_size = horizontal_size
		self.vertical_size = vertical_size
		self.board = []
		
	def fill_blank(self):
		self.horizontal_size = int(input("horizontal size? "))
		self.vertical_size = int(input("vertical size? "))
		
		for y in range(self.vertical_size):
			self.board.append([])
			self.board[y].append([" " for x in range(self.horizontal_size)])

	def hand_make(self):
		go = True
		self.board = []
		while go:
			row = input("row->")
			
			if 'z' in row or 'Z' in row:
				go = False
			
			else:
				nurow = []
				for item in row:
					if item != ' ':
						nurow.append(item)
					else:
						nurow.append('#')
				self.board.append(nurow)
			
		self.vertical_size = len(self.board)
		self.horizontal_size = len(self.board[0])
	
	def rand_make(self):
	#populates field with a percentage of live cels
		self.vertical_size = int(input("vertical size?   "))
		self.horizontal_size = int(input("horizontal size?   "))
		percentage = int(input("percent/100?   "))
		self.board = []
		print (percentage)
		for y in range(self.vertical_size):
			
			self.board.append([])
			for x in range(self.horizontal_size):
				cel = randint(0, 100)
				if cel > percentage:
					self.board[y].append(' ')
				else:
					self.board[y].append('#')
		
	
	def fill_in(self):
	
		for y in range(1, len(self.board)):
			amt = (len(self.board[0]) - len(self.board[y]))
			while amt > 0:
				self.board[y].append(' ')
				amt -= 1
			while amt < 0:
				self.board[y].pop()
				amt += 1
		
		for thismany in range(10):
			for item in self.board:
				item.insert(0, ' ')
		for item in self.board:
			item.extend([' ', ' ',' ', ' ',' ', ' ',' ', ' ',' ', ' '])
		for thismany in range(10):
			self.board.insert(0, [' ' for x in range(len(self.board[0]))])
		self.board.extend([[' ' for x in range(len(self.board[0]))]for x in range(10)])

		self.vertical_size += 20
		self.horizontal_size += 20
		
	def display(self):
		ystop = self.vertical_size - 10
		xstop = self.horizontal_size - 10
		bar = '   ' + ('=' * (xstop-7))
		print (bar)
		for y in range(10, ystop):
			print ('   |' + ''.join(self.board[y][10:xstop]) + '|')
		print (bar)
			
	def count_neighbors(self, x, y):
	#return number of neighbors   right, dnright, left, upleft, upright, dnleft, up, down 
		neighbors = []
		width = self.horizontal_size-1
		height = self.vertical_size-1
		if x != width:
			neighbors.append(self.board[y][x+1])
		if x != width and y != height:
			neighbors.append(self.board[y+1][x+1])
		if x != 0:
			neighbors.append(self.board[y][x-1])
		if x != 0 and y != 0:
			neighbors.append(self.board[y-1][x-1])
		if x != width and y != 0:
			neighbors.append(self.board[y-1][x+1])
		if x != 0 and y != height:
			neighbors.append(self.board[y+1][x-1])
		if y != 0:
			neighbors.append(self.board[y-1][x])
		if y != height:
			neighbors.append(self.board[y+1][x])
		
		return neighbors.count('#')
		
		
	def advance_board(self):
		new_board = []
		for y in range(len(self.board)):
			new_board.append([])
			for x in range(len(self.board[0])):
			
				num = self.count_neighbors(x, y)
				
				if num >= 4:
					new_board[y].append(' ')
				elif num >= 2 and self.board[y][x] == '#':
					new_board[y].append('#')
				elif num == 3 and self.board[y][x] == ' ':
					new_board[y].append('#')
				else:
					new_board[y].append(' ')
		
		return new_board
			
			
			
MyGame = LifeSpace(0, 0)
				
while True:
		if 'a' in input("for random fill type 'a'") :
			MyGame.rand_make()
		else:
			MyGame.hand_make()
			
		MyGame.fill_in()
		MyGame.display()
		
		while True:
			MyGame.board = MyGame.advance_board()
			MyGame.display()
			
			if input('') == "z":
				break
				
		if input('Enter for New, or Z to end>') == "z":
			break
		
