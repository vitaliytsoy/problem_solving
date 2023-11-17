"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""
from typing import List

class TrieNode:
    def __init__(self, edges, is_end):
        self.edges = edges
        self.is_end = is_end

class Trie:
    def __init__(self, wordsList):
        self.root_node = TrieNode({}, False)
        
        for word in wordsList:
            pointer = self.root_node
            
            for i in range(len(word)):
                letter = word[i]
                
                if letter not in pointer.edges:
                    pointer.edges[letter] = TrieNode({}, False)
            
                pointer = pointer.edges[letter]
                
                if i == len(word) - 1:
                    pointer.is_end = True
                    
    def startsFrom(self, string):
        pointer = self.root_node
        
        for s in string:
            if s not in pointer.edges:
                return (False, False)
            
            pointer = pointer.edges[s]            
            
        return (True, pointer.is_end)


class Solution:
    def search_word_break(self, s: str, trie: Trie) -> bool:
        temp = ''
        
        if s == '':
            return True
        
        for i in range(len(s)):
            letter = s[i]
            temp += letter
            
            is_starting_from, is_end_word = trie.startsFrom(temp)
            
            if (not is_starting_from):
                return False
            
            if (not is_end_word):
                continue
            
            if self.search_word_break(s[i + 1:], trie):
                return True
    
        return False
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie(wordDict)
                
        return self.search_word_break(s, trie)
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_start = [False] * (len(s) + 1)
        word_end = [False] * (len(s) + 1)
        trie = Trie(wordDict)
        wordDict = set(wordDict)
        i = 0
        
        while i < len(s):
            if not word_end[i] and i != 0:
                i += 1
                continue

            for j in range(i + 1, len(s) + 1):
                word = s[i : j]
                is_starting_from, is_end_word = trie.startsFrom(word)


                if not is_starting_from:
                    break
                        
                if is_end_word:
                    word_start[i] = True
                    word_end[j] = True
    
            i += 1
                    
        if not word_start[0] or not word_end[-1]:
            return False
        
        pointer = 1
        
        while pointer < len(s):
            if word_end[pointer] ^ word_start[pointer]:
                start = pointer - 1
                end = pointer + 1
                    
                while not word_end[end]:
                    end += 1
                    
                while start >= 0:
                    if start < 0:
                        return False
                    
                    if (word_start[start] and s[start : end] in wordDict):
                        pointer += 1
                        break
                    
                    start -= 1
            
            pointer += 1
        
        return True
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        word_end = [False] * (len(s) + 1)
        word_end[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i, 0, -1):
                if word_end[j - 1] and s[j-1:i] in wordDict:
                    word_end[i] = True
                    break
                
        return word_end[-1]
    
s = Solution()
print(s.wordBreak('leetcode', ["leet","code"])) # True
print(s.wordBreak('applepenapple', ["apple","pen"])) # True
print(s.wordBreak('catsandog', ["cats","dog","sand","and","cat"])) # False
print(s.wordBreak('bb', ["a","b","bbb","bbbb"])) # True
print(s.wordBreak("aaaaaaa", ["aaaa","aa"])) # False
print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
print(s.wordBreak("abcd", ["a","abc","b","cd"])) # True
print(s.wordBreak("cars", ["car","ca","rs"])) # True
print(s.wordBreak("catsandogcat", ["cats","dog","sand","and","cat","an"])) # True
print(s.wordBreak("fohhemkkaecojceoaejkkoedkofhmohkcjmkggcmnami", ["kfomka","hecagbngambii","anobmnikj","c","nnkmfelneemfgcl","ah","bgomgohl","lcbjbg","ebjfoiddndih","hjknoamjbfhckb","eioldlijmmla","nbekmcnakif","fgahmihodolmhbi","gnjfe","hk","b","jbfgm","ecojceoaejkkoed","cemodhmbcmgl","j","gdcnjj","kolaijoicbc","liibjjcini","lmbenj","eklingemgdjncaa","m","hkh","fblb","fk","nnfkfanaga","eldjml","iejn","gbmjfdooeeko","jafogijka","ngnfggojmhclkjd","bfagnfclg","imkeobcdidiifbm","ogeo","gicjog","cjnibenelm","ogoloc","edciifkaff","kbeeg","nebn","jdd","aeojhclmdn","dilbhl","dkk","bgmck","ohgkefkadonafg","labem","fheoglj","gkcanacfjfhogjc","eglkcddd","lelelihakeh","hhjijfiodfi","enehbibnhfjd","gkm","ggj","ag","hhhjogk","lllicdhihn","goakjjnk","lhbn","fhheedadamlnedh","bin","cl","ggjljjjf","fdcdaobhlhgj","nijlf","i","gaemagobjfc","dg","g","jhlelodgeekj","hcimohlni","fdoiohikhacgb","k","doiaigclm","bdfaoncbhfkdbjd","f","jaikbciac","cjgadmfoodmba","molokllh","gfkngeebnggo","lahd","n","ehfngoc","lejfcee","kofhmoh","cgda","de","kljnicikjeh","edomdbibhif","jehdkgmmofihdi","hifcjkloebel","gcghgbemjege","kobhhefbbb","aaikgaolhllhlm","akg","kmmikgkhnn","dnamfhaf","mjhj","ifadcgmgjaa","acnjehgkflgkd","bjj","maihjn","ojakklhl","ign","jhd","kndkhbebgh","amljjfeahcdlfdg","fnboolobch","gcclgcoaojc","kfokbbkllmcd","fec","dljma","noa","cfjie","fohhemkka","bfaldajf","nbk","kmbnjoalnhki","ccieabbnlhbjmj","nmacelialookal","hdlefnbmgklo","bfbblofk","doohocnadd","klmed","e","hkkcmbljlojkghm","jjiadlgf","ogadjhambjikce","bglghjndlk","gackokkbhj","oofohdogb","leiolllnjj","edekdnibja","gjhglilocif","ccfnfjalchc","gl","ihee","cfgccdmecem","mdmcdgjelhgk","laboglchdhbk","ajmiim","cebhalkngloae","hgohednmkahdi","ddiecjnkmgbbei","ajaengmcdlbk","kgg","ndchkjdn","heklaamafiomea","ehg","imelcifnhkae","hcgadilb","elndjcodnhcc","nkjd","gjnfkogkjeobo","eolega","lm","jddfkfbbbhia","cddmfeckheeo","bfnmaalmjdb","fbcg","ko","mojfj","kk","bbljjnnikdhg","l","calbc","mkekn","ejlhdk","hkebdiebecf","emhelbbda","mlba","ckjmih","odfacclfl","lgfjjbgookmnoe","begnkogf","gakojeblk","bfflcmdko","cfdclljcg","ho","fo","acmi","oemknmffgcio","mlkhk","kfhkndmdojhidg","ckfcibmnikn","dgoecamdliaeeoa","ocealkbbec","kbmmihb","ncikad","hi","nccjbnldneijc","hgiccigeehmdl","dlfmjhmioa","kmff","gfhkd","okiamg","ekdbamm","fc","neg","cfmo","ccgahikbbl","khhoc","elbg","cbghbacjbfm","jkagbmfgemjfg","ijceidhhajmja","imibemhdg","ja","idkfd","ndogdkjjkf","fhic","ooajkki","fdnjhh","ba","jdlnidngkfffbmi","jddjfnnjoidcnm","kghljjikbacd","idllbbn","d","mgkajbnjedeiee","fbllleanknmoomb","lom","kofjmmjm","mcdlbglonin","gcnboanh","fggii","fdkbmic","bbiln","cdjcjhonjgiagkb","kooenbeoongcle","cecnlfbaanckdkj","fejlmog","fanekdneoaammb","maojbcegdamn","bcmanmjdeabdo","amloj","adgoej","jh","fhf","cogdljlgek","o","joeiajlioggj","oncal","lbgg","elainnbffk","hbdi","femcanllndoh","ke","hmib","nagfahhljh","ibifdlfeechcbal","knec","oegfcghlgalcnno","abiefmjldmln","mlfglgni","jkofhjeb","ifjbneblfldjel","nahhcimkjhjgb","cdgkbn","nnklfbeecgedie","gmllmjbodhgllc","hogollongjo","fmoinacebll","fkngbganmh","jgdblmhlmfij","fkkdjknahamcfb","aieakdokibj","hddlcdiailhd","iajhmg","jenocgo","embdib","dghbmljjogka","bahcggjgmlf","fb","jldkcfom","mfi","kdkke","odhbl","jin","kcjmkggcmnami","kofig","bid","ohnohi","fcbojdgoaoa","dj","ifkbmbod","dhdedohlghk","nmkeakohicfdjf","ahbifnnoaldgbj","egldeibiinoac","iehfhjjjmil","bmeimi","ombngooicknel","lfdkngobmik","ifjcjkfnmgjcnmi","fmf","aoeaa","an","ffgddcjblehhggo","hijfdcchdilcl","hacbaamkhblnkk","najefebghcbkjfl","hcnnlogjfmmjcma","njgcogemlnohl","ihejh","ej","ofn","ggcklj","omah","hg","obk","giig","cklna","lihaiollfnem","ionlnlhjckf","cfdlijnmgjoebl","dloehimen","acggkacahfhkdne","iecd","gn","odgbnalk","ahfhcd","dghlag","bchfe","dldblmnbifnmlo","cffhbijal","dbddifnojfibha","mhh","cjjol","fed","bhcnf","ciiibbedklnnk","ikniooicmm","ejf","ammeennkcdgbjco","jmhmd","cek","bjbhcmda","kfjmhbf","chjmmnea","ifccifn","naedmco","iohchafbega","kjejfhbco","anlhhhhg"])) # True


# a = '12345'

# for i in range(len(a)):
#     print(a[i])