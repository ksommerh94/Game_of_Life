from matrix import Board
'''
Karen Sommer
Feb 18 2022
Game of life
'''

def main():
    u_rows = 4#int(input('rows?'))
    u_columns = 4#int(input('columns?'))

    # create a board
    gol_board = Board(u_rows,u_columns)
    #initilize with positions
    initial = [(3,3),(2,2),(1,1),]
    gol_board.set_initial(initial)
    print("Initial matrix")
    gol_board.print_matrix_prev()
    print()
    #does changes
    gol_board.update_board()
    print("Final matrix")
    gol_board.print_matrix_curr()

main()
