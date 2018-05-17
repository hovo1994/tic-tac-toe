#!/usr/bin/env python
# Tic Tac Toe
from random import shuffle
board = [ '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
#board = ['O', 'X', ' ', 'O', ' ', 'X', 'O', 'X', 'X']
wins = [ [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1,
4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6] ]

def play():
	global board
	print 'Tc Tac Toe'
	print 'play against the computer AI level 0'
	print 'two players'
	printBoard()
	while True :
		wipeBoard()
		player_turn = 'X'
		while checkWin(swapPlayer(player_turn),board) == False and canMove() == True:
			# getMove(player_turn)
			if player_turn == 'X':
				getMove(player_turn)
			else:
				generateMove()
			printBoard()
			player_turn = swapPlayer(player_turn)
		if checkWin(swapPlayer(player_turn), board):
			print 'Player', swapPlayer(player_turn), 'wins New Game'
		else:
			print 'A draw.  New Game'

def generateMove():
	if canIwin():
		pass
	elif canYouWin():
		pass
	else:
		randomMove()

def randomMove():
	global board
	moves = list()
	for squares in range(0, len(board) ):
		if board[squares] == ' ':
			moves.append(squares)
	shuffle(moves)
	board[moves[0]] = 'O'
	print 'My move is ', moves[0] + 1

def canIwin():
	global board
	testBoard = board 
	moveMade = False
	for square in range(0, len(board)):
		if testBoard[square] == ' ' and moveMade == False:
			testBoard[square] = 'O'
			if checkWin('O', testBoard):
				board[square] = 'O'
				moveMade = True
				print 'My move is ', square + 1
			else:
				testBoard[square] = ' ' 
	return moveMade

def canYouWin():
	global board
	testBoard = board 
	moveMade = False
	for square in range(0, len(board)):
		if testBoard[square] == ' ' and moveMade == False:
			testBoard[square] = 'X'
			if checkWin('X', testBoard):
				board[square] = 'X'
				moveMade = True
				print 'My move is ', square + 1
			else:
				testBoard[square] = ' ' 
	return moveMade



def generateMove():
	global board 
	moves = list()
	for squares in range(0, len(board)):
		if board[squares] == ' ':
			moves.append(squares)
	shuffle(moves)
	board[moves[0]] = 'O'
	print 'My move is ', moves[0] + 1

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


def checkWin(player, board):
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