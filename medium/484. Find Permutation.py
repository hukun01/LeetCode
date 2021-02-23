# 484. Find Permutation
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        '''
        Greedy.
        In [1, n], the smallest permutation is [1,2,...,n].
        This is the permutation cloest to the final answer.
        To make the final answer as small as possible, we want to put the
        smallest numbers at the front. And we can do that by reversing the
        first 'D's in the string.
        For example, for s 'DDIID', we start with [1,2,3,4,5,6], and when
        seeing 'DD', we reverse the ans[0:3] to be [3,2,1,4,5,6], the next 'I'
        is handled because the ans[3] is greater than all values in ans[:3].
        Also, 'I's pattern is by default covered, as we start with an
        increasing sequence, so we just skip all 'I's, or we only process
        consecutive 'D's in the string.

        Time: O(n)
        Space: O(n)
        '''
        n = len(s)
        ans = list(range(1, n + 2))
        i = 1
        while i <= n:
            j = i
            while i <= n and s[i-1] == 'D':
                i += 1
            ans[j-1:i] = ans[j-1:i][::-1]
            i += 1
        return ans