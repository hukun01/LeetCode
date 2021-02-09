# 1754. Largest Merge Of Two Strings
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        '''
        Greedy.
        Build the answer char by char, always pick from the larger string.

        Same as the merge() in 321. Create Maximum Number
        '''
        A = deque(word1)
        B = deque(word2)

        return "".join(max(A, B).popleft() for _ in A + B)