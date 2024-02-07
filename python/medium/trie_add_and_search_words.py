"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
"""
from collections import deque

class LetterNode:
    def __init__(self):
        self.edges = {}
        self.is_end = False
    

class WordDictionary:
    def __init__(self):
        self.head = LetterNode()

    def addWord(self, word: str) -> None:
        pointer = self.head
        
        for letter in word:            
            if letter not in pointer.edges:
                pointer.edges[letter] = LetterNode()
            
            pointer = pointer.edges[letter]
            
        pointer.is_end = True
    
    def search(self, word):
        stack = deque()
        
        stack.append((self.head, word))

        while stack:
            pointer, word = stack.pop()
            
            if word == '':
                if pointer.is_end:
                    return True
                continue
            
            letter = word[0]
            
            if letter == '.':
                for edge in pointer.edges.values():
                    stack.append((edge, word[1:]))
                    
                continue
            
            if letter not in pointer.edges:
                continue
            
            stack.append((pointer.edges[letter], word[1:]))
            
        return False
    
    def search(self, word):
        node = self.head
        self.res = False
        self.dfs(node, word)
        return self.res
    
    def dfs(self, node, word):
        if not word:
            if node.is_end:
                self.res = True
            return 
        if word[0] == ".":
            for n in node.edges.values():
                self.dfs(n, word[1:])
        else:
            node = node.edges.get(word[0])
            if not node:
                return 
            self.dfs(node, word[1:])
        

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

s = WordDictionary()
print(s.addWord("bad")) 
print(s.addWord("dad")) 
print(s.addWord("mad")) 
print(s.search("pad")) 
print(s.search("bad")) 
print(s.search(".ad")) 
print(s.search("b..")) 

# Output
# [null,null,null,null,false,true,true,true]


# ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
# [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]

# Output
# [null,null,null,null,null,true,false,null,true,true,false,true,true,true]
# Expected
# [null,null,null,null,null,false,false,null,true,true,false,false,true,false]



class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
    
class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res
    
    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return 
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return 
            self.dfs(node, word[1:])
