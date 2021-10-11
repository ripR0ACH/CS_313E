class Queens(object):
	# init the board
	def __init__(self, n = 8):
		self.board = []
		self.n = n
		for i in range(self.n):
			row = []
			for j in range(self.n):
				row.append('*')
			self.board.append(row)
	
	# print the board
	def print_board(self):
		for i in range(self.n):
			for j in range(self.n):
				print(self.board[i][j], end = ' ')
			print()
		print()
	
	# check if no queen captures another
	def is_valid(self, row, col):
		for i in range(self.n):
			if self.board[row][i] == 'Q' or self.board[i][col] == 'Q':
				return False
		for i in range(self.n):
			for j in range(self.n):
				row_diff = abs(row - i)
				col_diff = abs(col - j)
				if row_diff == col_diff and self.board[i][j] == 'Q':
					return False
		return True

def main():
	# lambda with sort
	a = [(2, 2, 9), (2, 2, 3), (3, 2, 5), (2, 1, 4), (2, 2, 2), (4, 2, 1)]
	b = sorted(a, key = lambda x: (x[2], x[0], x[1]))
	print(a)
	print(b)

	# lambda with filter
	p = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
	q = list(filter(lambda x: x % 2 == 0, p))
	print(p)
	print(q)

	# lambda with map
	c = [39.2, 36.5, 37.3, 40.2, 37.9]
	f = list(map(lambda x: (9 * x) / 5 + 32, c))
	print(c)
	print(f)

main()
