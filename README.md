# Team TEA: Sudoku
## Introduction
As all of our members are interested in solving sudoku, our project is to explore the data structure and algorithm behind sudoku by solving the problem of generating a random 9*9 sudoku with exactly one unique solution and providing a User Interface to try the sudoku puzzle we generate. In addition, we compared the two algorithms for generating and solving sudoku: Dancing Link with Algorithm X (DLX) and Depth First Search (DFS), and the comparison between their performance is shown by plots. 

The process to achieve our goal is to first convert the sudoku problem to the Exact Cover problem and use Knuth's Algorithm X to find the solution to the Exact Cover problem. We can then solve the sudoku problem by that solution. To implement Knuth's Algorithm X, we implement the data structure, Dancing Links, from scratch instead of using 2D arrays to improve the runtime and performance. This project covers learning data structures and algorithms, which aligns with our expectation to learn some complex data structures and algorithms that might not be covered in class. 


## Instruction
### Performance Comparison


### Sudoku UI
1. Run the sudoku.py file
2. A window will show up with a solvable sudoku puzzle.
3. Click on the empty cell in the sudoku puzzle and input a number to it by keyboard.
4. Once finishing inputting all the empty cells, click on the “Check” button on the left to check if your solution is correct.
5. The window will show a small message below the “New” button informing your results of whether you solve the puzzle.
6. If you succeed, you can click on the “New” button to start a new game.
7. If you fail, you can click restart to retry the same game.
8. Finally, close the window to quit the game.
