#  File: RewardGrid.py
#  Description: find the most rewarding path to the finish only moving down and to the right
#  Student Name: zachary morrison
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
# DO NOT change name or header of best_reward
# down direction and right direction
def path(grid, pos, total):
    if pos[0] == len(grid) - 1 and pos[1] == len(grid[pos[0]]) - 1:
        return total + grid[pos[0]][pos[1]]
    if pos[0] + 1 < len(grid) and pos[1] + 1 < len(grid[pos[0]]):
        if path(grid, [pos[0] + 1, pos[1]], total + grid[pos[0]][pos[1]]) > path(grid, [pos[0], pos[1] + 1], total + grid[pos[0]][pos[1]]):
            return path(grid, [pos[0] + 1, pos[1]], total + grid[pos[0]][pos[1]])
        else: 
            return path(grid, [pos[0], pos[1] + 1], total + grid[pos[0]][pos[1]])
    elif pos[0] + 1 < len(grid):
        return path(grid, [pos[0] + 1, pos[1]], total + grid[pos[0]][pos[1]])
    elif pos[1] + 1 < len(grid[pos[0]]):
        return path(grid, [pos[0], pos[1] + 1], total + grid[pos[0]][pos[1]])
    return total
        
def best_reward(grid):
    # given 2d grid, return cost of maximum path from the top left to the bottom right
    # you can only move down and right
    return path(grid, [0, 0], 0)
if __name__ == "__main__":
  # write debug statements, test cases, etc (use assert statements)
  # this code will not be run on the autograder, only best_reward will be tested
  pass