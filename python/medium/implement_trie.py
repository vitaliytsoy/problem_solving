"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
"""
class TrieNode:
    def __init__(self):
        self.edges = {}
        self.is_end_node = False

class Trie:    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        pointer = self.root
        
        for index in range(len(word)):
            letter = word[index]
            
            if (letter not in pointer.edges): 
                pointer.edges[letter] = TrieNode()
            
            pointer = pointer.edges[letter]
        
            if (index == len(word) - 1):
                pointer.is_end_node = True

    def search(self, word: str) -> bool:
        pointer = self.root
        
        for index in range(len(word)):
            letter = word[index]
            
            if letter not in pointer.edges:
                return False
            
            if index == len(word) - 1 and not pointer.edges[letter].is_end_node:
                return False
            
            pointer = pointer.edges[letter]
        
        return True
                
    def startsWith(self, prefix: str) -> bool:
        pointer = self.root
        
        for letter in prefix: 
            if (letter in pointer.edges):
                pointer = pointer.edges[letter]
                continue;
            
            return False
        
        return True
    

        


# Your Trie object will be instantiated and called as such:
trie = Trie()

# print("insert apple", trie.insert("apple"))
# print("search apple", trie.search("apple"))
# print("search app", trie.search("app"))
# print("startsWith app", trie.startsWith("app"))
# print("insert app", trie.insert("app"))
# print("search app", trie.search("app"))


print("startsWith a", trie.startsWith("a"))
  