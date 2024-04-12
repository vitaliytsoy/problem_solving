"""
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

Example 1:

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

Example 2:

Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6
"""
from typing import List
from collections import deque

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = []
        result_capital = w
        
        for i in range(len(capital)):
            projects.append((capital[i], profits[i]))
            
        projects.sort()
        
        for i in range(k):
            pointer = -1
            
            for j in range(len(projects)):
                if projects[j][0] > result_capital:
                    break
                
                pointer = j
                
            available_projects = projects[0:pointer + 1]
            max_profit_project = (-1, -1)
            
            if not available_projects:
                break

            for j in range(len(available_projects)):
                capital, profit = available_projects[j]
                
                if profit >= max_profit_project[1]:
                    max_profit_project = (j, profit)
                    
            m_index, m_profit = max_profit_project    
            result_capital += m_profit
        
            max_profit_project= (-1, -1)
            projects.pop(m_index)
                    
        return result_capital


s = Solution()
# print(s.findMaximizedCapital(2, 0, [1,2,3], [0,1,1])) # 4
# print(s.findMaximizedCapital(3, 0, [1,2,3], [0,1,2])) # 6
print(s.findMaximizedCapital(1, 0, [1,2,3], [1,1,2])) # 0
# print(s.findMaximizedCapital(2, 0, [1,2,3], [0,1,1])) # 4
