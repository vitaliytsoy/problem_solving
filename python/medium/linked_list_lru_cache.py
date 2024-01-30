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
class CacheNode: 
    def __init__(self, key = 0, value = 0, prev_node = None, next_node = None):
        self.value = value
        self.key = key
        self.prev = prev_node
        self.next = next_node

class LRUCache:
    def __init__(self, capacity: int):
        self.head = CacheNode()
        self.tail = self.head
        self.capacity = capacity
        self.mapper = {}
        
    def add(self, key, value):
        new_node = CacheNode(key, value, self.tail, None)
            
        self.mapper[key] = new_node
        self.tail.next = new_node
        self.tail = self.tail.next
        
        return new_node
            
    def remove_lru_node(self):
        del_node = self.head.next
        next_del_node = del_node.next
        
        if del_node == self.tail:
            self.tail = del_node.prev
        
        self.head.next = next_del_node
        
        del_node.next = None
        del_node.prev = None

        if next_del_node:
            next_del_node.prev = self.head

        del self.mapper[del_node.key]
        
            
    def move_to_tail(self, key):
        node = self.mapper[key]
        prev_node = node.prev
        next_node = node.next
        
        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node
            
            self.tail.next = node 
            node.prev = self.tail
            node.next = None
            self.tail = self.tail.next
            
        return node
        
        
    def get(self, key: int) -> int:
        if key in self.mapper:
            node = self.move_to_tail(key)
            
            return node.value
               
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None
        
        if key in self.mapper:
            node = self.move_to_tail(key)
            
            if value != node.value:
                node.value = value            
            
            return None
        
        if len(self.mapper.keys()) < self.capacity:
            self.add(key, value)
            
            return None
        
        self.remove_lru_node()
        self.add(key, value)

        return None
        
# [[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]
# [null,null,null,null,4,3,2,-1,null,-1,2,3,-1,5]

# s = LRUCache(3)
# print(s.put(1,1))
# print(s.put(2,2))
# print(s.put(3,3))
# print(s.put(4,4))
# print(s.get(4))
# print(s.get(3))
# print(s.get(2))
# print(s.get(1))
# print(s.put(5,5))
# print(s.get(1))
# print(s.get(2))
# print(s.get(3))
# print(s.get(4))
# print(s.get(5))


#[[1],[2,1],[2],[3,2],[2],[3]]
#[null,null,1,null,-1,2]

# s = LRUCache(1)
# print(s.put(2,1)) 
# print(s.get(2)) 
# print(s.put(3,2))
# print(s.get(2))
# print(s.get(3))


# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
# [null,null,null,1,null,-1,null,-1,3,4]

# s = LRUCache(2)
# print(s.put(1,1))
# print(s.put(2,2))
# print(s.get(1))
# print(s.put(3,3))
# print(s.get(2))
# print(s.put(4,4))
# print(s.get(1))
# print(s.get(3))
# print(s.get(4))



#[[1],[6],[8],[12,1],[2],[15,11],[5,2],[1,15],[4,2],[5],[15,15]]
#[null,-1,-1,null,-1,null,null,null,null,-1,null]
s = LRUCache(1)
print(s.get(6))
print(s.get(8))
print(s.put(12,1))
print(s.get(2))
print(s.put(15,11))
print(s.put(5,2))
print(s.put(1,15))
print(s.put(4,2))
print(s.get(5))
print(s.put(15,15))







