# 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        1/2 Greedy. The key is to write concise code.
        '''
        s_idx = t_idx = 0
        while s_idx < len(s) and t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            t_idx += 1
        return s_idx == len(s)
        '''
        2/2 Binary search with time O(T) + O(S*log(T))
        This is better at handling scenarios where there are many 's' but one 't'.

        Record the indicies of each char in t, scan through s, for each char,
        find all its positions in t, and binary search the smallest position that
        is greater the previous index of the previous char.
        If there's such an index, set the prev index with it, otherwise return False.
        '''
        idx = defaultdict(list)
        for i, c in enumerate(t):
            idx[c].append(i)
        print(idx)
        prev = 0
        for i, c in enumerate(s):            
            j = bisect.bisect_left(idx[c], prev)
            if j == len(idx[c]): return False
            print(f"prev {prev}")
            print(f"j {j}")
            prev = idx[c][j] + 1
        return True