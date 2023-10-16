"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
"""
from typing import List
from collections import deque
import sys 

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        stack = deque([(startGene, endGene, 0)])
        genes_mutations = set([startGene])
        genes = ["A", "C", "G", "T"]
        min_reach_mutation = {}
        min_count = sys.maxsize
        
        while stack:
            a_gene, b_gene, count = stack.pop()
            
            if (a_gene == b_gene):
                min_count = min(min_count, count)
                continue
    
            for i in range(len(a_gene)):
                a_list = list(a_gene)
                
                for gene in genes:
                    c_gene = a_list.copy()
                    c_gene[i] = gene
                    c_gene = ''.join(c_gene)
                    
                    if c_gene in min_reach_mutation and min_reach_mutation[c_gene] < count + 1:
                        continue
                    else:
                        min_reach_mutation[c_gene] = count + 1
                    
                    if c_gene in bank:
                        genes_mutations.add(c_gene)
                        stack.append((c_gene, b_gene, count + 1))
                    
        return -1 if min_count == sys.maxsize else min_count
                    
s = Solution()

print(s.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"])) # 1
print(s.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"])) # 2
print(s.minMutation("AACCGGTT", "AAACGGTA", ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"])) # 4
print(s.minMutation("AAAACCCC", "CCCCCCCC", ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"])) # 4
