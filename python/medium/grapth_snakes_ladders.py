"""
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.

Example 1:

Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.

Example 2:

Input: board = [[-1,-1],[-1,3]]
Output: 1
"""
from typing import List
from collections import deque
import sys 

class Solution:    
    def convert_step_to_index(self, step, n):    
        i = (step - 1) // n
        j = (step - 1) % n

        return (i, j)
    
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board_size = len(board)
        last_step = board_size ** 2
        queue = deque([(1, 0)])
        dice_rolls = [6,5,4,3,2,1]
        min_steps = sys.maxsize

        board.reverse()
                
        for i in range(board_size):
            if i % 2 != 0:
                board[i].reverse()
                
        while queue:
            step, count = queue.popleft()
            is_rolled_empty = False
            
            if (step >= last_step):
                min_steps = min(min_steps, count)
                
            
            for roll in dice_rolls:
                rolled = step + roll
                
                if rolled > last_step:
                    continue

                i, j = self.convert_step_to_index(rolled, board_size)
                teleport = board[i][j]
                
                if (teleport == '#'):
                    continue
                
                if (teleport != -1):
                    board[i][j] = '#'
                    queue.append((teleport, count + 1))
                    continue
                
                if (is_rolled_empty): 
                    continue
                
                is_rolled_empty = True
                queue.append((step + roll, count + 1))
                
        return -1 if min_steps == sys.maxsize else min_steps
    
s = Solution()
# 4 1 1 -1 2 4 3 3 10 4
print(s.snakesAndLadders(
    [
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,35,-1,-1,13,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,15,-1,-1,-1,-1]
        ]
)) # 4
print(s.snakesAndLadders([[-1,-1],[-1,3]])) # 1
print(s.snakesAndLadders([[-1,7,-1],[-1,6,9],[-1,-1,2]])) # 1
print(s.snakesAndLadders([[1,1,-1],[1,1,1],[-1,1,1]])) # -1
print(s.snakesAndLadders([[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]])) # 2
print(s.snakesAndLadders([
    [-1,-1,-1,46,47,-1,-1,-1],
    [51,-1,-1,63,-1,31,21,-1],
    [-1,-1,26,-1,-1,38,-1,-1],
    [-1,-1,11,-1,14,23,56,57],
    [11,-1,-1,-1,49,36,-1,48],
    [-1,-1,-1,33,56,-1,57,21],
    [-1,-1,-1,-1,-1,-1,2,-1],
    [-1,-1,-1,8,3,-1,6,56]
])) # 4
print(s.snakesAndLadders([
    [-1,-1,-1,-1,48,5,-1],
    [12,29,13,9,-1,2,32],
    [-1,-1,21,7,-1,12,49],
    [42,37,21,40,-1,22,12],
    [42,-1,2,-1,-1,-1,6],
    [39,-1,35,-1,-1,39,-1],
    [-1,36,-1,-1,-1,-1,5]
])) # 3
print(s.snakesAndLadders(
    [
        [-1,10,-1,15,-1],
        [-1,-1,18,2,20],
        [-1,-1,12,-1,-1],
        [2,4,11,18,8],
        [-1,-1,-1,-1,-1]
    ]
)) # 3
print(s.snakesAndLadders(
    [
        [-1,-1,-1,135,-1,-1,-1,-1,-1,185,-1,-1,-1,-1,105,-1],
        [-1,-1,92,-1,-1,-1,-1,-1,-1,201,-1,118,-1,-1,183,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1,179,-1,-1,-1,-1,-1,-1],
        [-1,248,-1,-1,-1,-1,-1,-1,-1,119,-1,-1,-1,-1,-1,192],
        [-1,-1,104,-1,-1,-1,-1,-1,-1,-1,165,-1,-1,206,104,-1],
        [145,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,229,-1],
        [-1,-1,75,140,-1,-1,-1,-1,-1,-1,-1,-1,43,-1,34,-1],
        [-1,-1,-1,-1,-1,-1,169,-1,-1,-1,-1,-1,-1,188,-1,-1],
        [-1,-1,-1,-1,-1,-1,92,-1,171,-1,-1,-1,-1,-1,-1,66],
        [-1,-1,-1,126,-1,-1,68,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,109,-1,86,28,228,-1,-1,144,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,59,-1,-1,-1,-1,-1,51,-1,-1,-1,62,-1],
        [-1,71,-1,-1,-1,63,-1,-1,-1,-1,-1,-1,212,-1,-1,-1],
        [-1,-1,-1,-1,174,-1,59,-1,-1,-1,-1,-1,-1,133,-1,-1],
        [-1,-1,62,-1,5,-1,16,-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,59,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    ]
)) # 10

print(s.snakesAndLadders(
    [
        [-1,18,-1,-1,-1,-1,-1,-1,-1,68,-1],
        [-1,-1,99,24,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,109,-1,-1,-1,4,93,-1,79,103],
        [-1,-1,-1,-1,-1,-1,-1,-1,107,-1,107],
        [37,34,-1,-1,64,-1,-1,-1,-1,119,56],
        [-1,-1,-1,-1,-1,-1,64,-1,-1,-1,-1],
        [-1,-1,-1,96,-1,-1,-1,-1,107,-1,-1],
        [-1,91,-1,103,11,54,-1,114,36,121,-1],
        [-1,72,69,42,-1,-1,-1,-1,-1,-1,81],
        [79,-1,-1,-1,-1,47,-1,97,75,75,-1],
        [-1,-1,-1,-1,-1,-1,-1,71,-1,-1,-1]
    ]
)) # 4



