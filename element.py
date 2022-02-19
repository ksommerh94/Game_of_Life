'''
Karen Sommer
Feb 18 2022
Game of life
'''

#Class element, stores prev value , current/new value and the position in the matrix
class Element:
    #constructor of element, this class contains prev_val and current, and the position in the matrix
    #params: prev_value , the initialized value , row: position in the matrix , col: position in the matrix
    def __init__(self,prev_val,row,col):
        self.prev_val = prev_val
        self.current_val = None
        self.position = (row,col)
