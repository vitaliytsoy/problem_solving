"""
Design a map that allows you to do the following:

Maps a string key to a given value.
Returns the sum of the values that have a key with a prefix equal to a given string.
Implement the MapSum class:

MapSum() Initializes the MapSum object.
void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.
 

Example 1:

Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
"""

from collections import deque

class TrieNode:
    def __init__(self):
        self.edges = {}
        self.value = 0
        self.is_end = False

class MapSum:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        pointer = self.root
        
        for index, letter in enumerate(key):
            if letter not in pointer.edges:
                pointer.edges[letter] = TrieNode()

            pointer = pointer.edges[letter]
            
            if index + 1 == len(key):
                pointer.is_end = True
                pointer.value = val

    def sum(self, prefix: str) -> int:
        result = 0
        pointer = self.root
        
        for letter in prefix:
            if (letter not in pointer.edges):
                return 0
            
            pointer = pointer.edges[letter]
            
        stack = deque([pointer])
            
        while stack:
            node = stack.pop()
            
            if (node.is_end):
                result += node.value
                
            for letter in node.edges:
                stack.append(node.edges[letter])
                
                
        return result
                


# Your MapSum object will be instantiated and called as such:
mapSum = MapSum()
# mapSum.insert("apple", 3)  
# print(mapSum.sum("ap"))           # return 3 (apple = 3)
# mapSum.insert("app", 2)    
# print(mapSum.sum("ap"))           # return 5 (apple + app = 3 + 2 = 5)

[[],["apple",3],["ap"],["app",2],["apple",2],["ap"]]
mapSum.insert("apple", 3);  
print(mapSum.sum("ap"))
mapSum.insert("app", 2)    
print(mapSum.sum("ap"))
mapSum.insert("apple", 2)    
print(mapSum.sum("ap"))