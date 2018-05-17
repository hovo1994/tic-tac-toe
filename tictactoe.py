#!/usr/bin/env python
# Tic Tac Toe
board = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
#board = ['O', 'X', ' ', 'O', ' ', 'X', 'O', 'X', 'X']
wins = [ [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1,
4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6] ]

def play():
	printBoard()
	print 'Tc Tac Toe'
	print 'two players'
	while True :
		wipeBoard()
		player_turn = 'X'
		while checkWin(swapPlayer(player_turn)) == False and canMove() == True:
			getMove(player_turn)
			printBoard()
			player_turn = swapPlayer(player_turn)
		if checkWin(swapPlayer(player_turn)):
			print 'Player', swapPlayer(player_turn), 'wins New Game'
		else:
			print 'A draw.  New Game'

def swapPlayer(player):
	if player == 'X':
		player = 'O'
	else:
		player = 'X'
	return player

def getMove(player):
	global board
	correct_number = False
	while correct_number == False:
		square = raw_input('Square to place the ' + player + ' ')
		try:
			square = int(square)
		except:
			square = -2
		square -= 1
		if square >= 0 and square < 10:
			if board[square] == ' ':
				board[square] = player
				correct_number = True
			else:
				print 'Square already occupied'
		else:
			print 'incorrect square try again'


def printBoard():
	print
	print '|',
	for square in range(0, 9):
		print board[square], '|',
		if square == 2 or square == 5:
			print
			print '-------------'
			print '|',
	print
	print


def checkWin(player):
	win = False
	for test in wins :
		count = 0
		for squares in test :
			if board[squares] == player :
				count += 1
			if count == 3 :
				win = True
	return win

def wipeBoard():
	global board
	for square in range(0, len(board)) :
		board[square] = ' '

def canMove():
	move = False
	for square in range(0, len(board)) :
		if board[square] == ' ':
			move = True
	return move

if __name__ == '__main__':
	play()