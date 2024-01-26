"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""
from collections import deque
import heapq

class CacheNode: 
    def __init__(self, value, use_index):
        self.value = value
        self.use_index = use_index


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = {}
        self.lru_map = {}
        self.lru_heap = []
        self.use_index = 1
        
        heapq.heapify(self.storage)

    def get(self, key: int) -> int:
        if key in self.storage:            
            self.storage[key].use_index = self.use_index
            self.lru_map[self.use_index] = key
            self.use_index += 1
                    
            return self.storage[key].value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.storage.keys()) < self.capacity:
            self.storage[key] = CacheNode(value, self.use_index)
            self.lru_map[self.use_index] = key
            self.use_index += 1
            
            return None
        
        # self.storage[self.lru_map[self.lru_index]] = CacheNode(value, self.use_index)
        self.lru_map[self.use_index] = key
        self.use_index += 1
        
        return None
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)