from element import Element
'''
Karen Sommer
Feb 18 2022
Game of life
'''

#Class borad, stores row , column and matrix of the game
class Board:

    #constructor of board game, initialize the matrix with the element and prev value in 0
    #params: row: amount of row col: amoutn  of columns
    def __init__(self,rows,cols):
        self.row = rows
        self.col = cols
        self.matrix = [[Element(0,r,c) for r in range(rows)] for c in range(cols)]

    #initialize board with the standing first positions
    #params: initial , list of tuples with positions on the matrix, updates the element previous value
    #return:none
    def set_initial(self,initial):
        for i in initial:
            if i[0] < 0 or i[0] >= self.row:
                continue
            elif i[1] < 0 or i[1] >= self.col:
                continue
            else:
                element = self.matrix[i[0]][i[1]]
                element.prev_val = 1
        return


    #print the matrix with previous values
    #params: none
    #return : none
    def print_matrix_prev(self):
        for row in range((self.row)):
            for col in range(self.col):
                print (self.matrix[row][col].prev_val,end='')
            print()
        return
    #print the matrix with current/new values
    #params: none
    #return none
    def print_matrix_curr(self):
        for row in range((self.row)):
            for col in range(self.col):
                print (self.matrix[row][col].current_val,end='')
            print()
        return

    #verifies each position
    #params: none
    #return: none
    def update_board(self):
        for r in range(self.row):
            for c in range(self.col):
                self.check_neighbour(r,c)
        return

    #checks every valid neighbor of every position in matrix
    #params: init_row = row we are standing to check the neighbours  init_col= col we are standing to check the neighbours
    #return: none
    def check_neighbour(self,init_row,init_col):
        neighbours = self.get_amount_neighbour(init_row,init_col)
        #change dead to live, 3 live neighbors
        if self.matrix[init_row][init_col].prev_val == 0:
             if neighbours == 3:
                 self.matrix[init_row][init_col].current_val = 1
             else:
                 self.matrix[init_row][init_col].current_val = 0

        else:
            #live cell with fewer than two live neighbors dies
            if neighbours < 2:
                self.matrix[init_row][init_col].current_val = 0
            #live cell with more than three live neighbors dies
            elif neighbours > 3:
                self.matrix[init_row][init_col].current_val = 0
            else:
                self.matrix[init_row][init_col].current_val = 1

        return

    #return the amount of neighbours each position has
    #params: init_row = row we are standing to check the neighbours  init_col= col we are standing to check the neighbours
    #return: amount of live neighbors
    def get_amount_neighbour(self,init_row,init_col):
        times = 0
        for row in range(-1,2):
            for col in range(-1,2):
                check_r = init_row + row
                check_c = init_col + col
                #print("row_ckec",check_r, "col_chck",check_c)
                if check_r < 0 or check_c < 0 or check_r >= self.row or check_c >= self.col:
                    continue
                if check_r == init_row and init_col == check_c:
                    continue
                else:
                    times += self.matrix[check_r][check_c].prev_val
        return times
