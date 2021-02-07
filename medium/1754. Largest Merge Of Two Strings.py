# 1754. Largest Merge Of Two Strings
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        '''
        Greedy.
        Build the answer char by char, always pick from the larger string.

        Same as the merge() in 321. Create Maximum Number
        '''
        A = list(word1)
        B = list(word2)

        return "".join(max(A, B).pop(0) for _ in A + B)