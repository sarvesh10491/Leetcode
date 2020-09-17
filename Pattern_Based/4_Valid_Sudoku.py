class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cd = {}         # Dictionary to track history of number seen in same column
        grid = {}       # Dictionary to track history of number seen in same grid
        cur_grid = -1
        
        for k in range(1,10):   # Value of these dictionaries will be list for each column/grid position from 1 to 9
            cd[str(k)] = []
            grid[k] = []
        
        for r in range(len(board)):
            rd = {}                             # Dictionary to track history of number seen in same row
            for c in range(len(board[0])):
                n = board[r][c]
                
                # Determine correct grid number we are in
                if r<3:
                    if c<3: cur_grid = 1
                    elif c<6: cur_grid = 2
                    else: cur_grid = 3
                elif r<6:
                    if c<3: cur_grid = 4
                    elif c<6: cur_grid = 5
                    else: cur_grid = 6
                else:
                    if c<3: cur_grid = 7
                    elif c<6: cur_grid = 8
                    else: cur_grid = 9
                
                if n!=".":
                    if n in rd or c in cd[n] or n in grid[cur_grid]:    # If number was seen in same row or column or grid, then its not valid sudoku
                        return False
                    rd[n] = 1                   # Update number was seen in current row
                    cd[n].append(c)             # Update number was seen in current column
                    grid[cur_grid].append(n)    # Update number was seen in current grid
                
        return True
        