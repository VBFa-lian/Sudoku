from copy import deepcopy
import numpy as np

#program ustalizes a Depth First Search data analysis structure for solving sudoku solution.
#Converts a text file containing one sudoku problem into a list of possible solutions 
#for each possibility of each square a new "branch" is explored completely until it leads to a solution or not. 


#begins the recursive function
def sudoku_solver_help(sudoku_dic):
    grid = load_sudoku_from_dict(sudoku_dic)
    solution = sudoku_solver(grid)
    return return_solns(solution)
    
#recursive sudoku solver function 
def sudoku_solver(grid):
    for i in range(len(grid)): 
        for j in range(len(grid)): 
            if len(grid[i, j]) == 1: 
                valid_grid(grid, i,j, grid[i, j][0])
    solved_board = True
    #checks if the board is unsolvable with no avaliable solutions for a square 
    for i in range(len(grid)):
        for j in range(len(grid)):
            if len(grid[i, j]) == 0:
                #print('wrong!')
                return None
            elif len(grid[i, j]) != 1:
                solved_board = False
    #if a solution is found then return 
    if solved_board:
        return grid
    else:
        for i in range(len(grid)):
            for j in range(len(grid)):
                if len(grid[i, j]) > 1:
                    for val in grid[i, j]:
                        new_board = deepcopy(grid)
                        valid_grid(new_board, i,j,val)
                        res = sudoku_solver(new_board)
                        if res is not None:
                            return res
                    #print('wrong!')
                    return None
                

#check if current value being put into the grid is valid 
#checks it against row, column and square 
#removes the value from list of possible values for each item in the grid
def valid_grid(grid,x,y, num):
    #check row
    for i in range(9):
        if num in grid[x, i]:
            grid[x, i].remove(num)
    #check col
    for i in range(9):
        if num in grid[i, y]:
            grid[i, y].remove(num)
    #check square
    square_start_col = (x//3)*3
    square_start_row = (y//3)*3
    for j in range(square_start_col, square_start_col + 3):
        for k in range(square_start_row, square_start_row +3):
            if (num in grid[j, k]):
                grid[j, k].remove(num)
    grid[x, y] = [num]
    
def return_solns(grid):
    sudoku = np.zeros((9, 9), int)
    for r in range(len(grid)):
        for c in range(len(grid)):
            sudoku[r, c] = grid[r, c][0]
    return sudoku

def load_sudoku_from_dict(dic: dict):
    grid = np.empty((9, 9), list)
    for r in range(9):
        for c in range(9):
            if (r, c) in dic.keys():
                grid[r, c] = [dic[(r, c)]]
            else:
                grid[r, c] = list(range(1, 10))
    return grid


#load the file of sudoku start
def load_sudoku_from_file():
    #load a single sudoku file from a file name 
    # Assuming a standard 9x9 Sudoku puzzle
    grid = np.empty((9, 9), list)
    with open('sudoku_files.txt', 'r') as file:
        for r in range(9):
            line = file.readline().strip() # Remove newline characters
            for c in range(len(line)):  
                if line[c] == '0':
                    # Cell is empty, add all possibilities
                    grid[r, c] = list(range(1, 10))
                else:
                    # Cell has a fixed number, add it as the only possibility
                    grid[r, c] = [int(line[c])]
    return grid