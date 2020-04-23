# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1='x'
p2='o'

def check_row(symbol):
    for r in range(3):
         count=0
         for c in range(3):
             if board[r][c]==symbol:
                 count=count+1
         if count==3:
             print(symbol,'WON')
             return True
    return False

def check_col(symbol):
    for c in range(3):
         count=0
         for r in range(3):
             if board[r][c]==symbol:
                 count=count+1
         if count==3:
             print(symbol,'WON')
             return True
    return False

def check_dia(symbol):
    if board[0][0]==board[1][1]==board[2][2]==symbol:
        print(symbol,'WON')
        return True
    if board[0][2]==board[1][1]==board[2][0]==symbol:
        print(symbol,'WON')
        return True
    else:
        return False


def place(symbol):
    print(numpy.matrix(board))
    while(1): 
        row=int(input('enter row 1-2-3'))
        col=int(input('nneter column 1-2-3'))
        if(row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-'):
            break
        else:
            print('invalid input')
    board[row-1][col-1]=symbol
    
def won(symbol):
    return check_row(symbol) or check_col(symbol) or check_dia(symbol)

def play():
    for turn in range(9):
        if(turn%2==0):
            print("x turn")
            place(p1)
            if won(p1):
                break
        else:
            print("o turn")
            place(p2)
            if won(p2):
                break
        if not(won(p1)) and not(won(p2)):
            print(' match is draw')
        
        
        
        
        
play()