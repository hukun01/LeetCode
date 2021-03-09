# 1754. Largest Merge Of Two Strings
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        '''
        Greedy.
        The key is to pick from word1 when word1 and word2 share the same
        prefix, but word1's later char is greater. E.g., word1 = 'aac', and
        word2 = 'aab'. And this can get complicated, e.g., if word1 = 'ccccc',
        and word2 = 'ccbx', after picking 'c' from word1, the next char should
        still be 'c' from word1, then 'c' from word1, now word1 = 'cc', word2
        didn't change, and word1 and word2 share the prefix which is also the
        full word1, in this case, we need to pick from word2, because the next
        char is 'b' from word2, and is greater than empty char. But we can only
        pick chars one by one from word2, because the relative order between
        word1 and word2 may change as each word changes, in this case, when we
        take 'c' from word2, it becomes 'cbx' which is less than word1 = 'cc',
        and when we take 'c' from word1, it becomes 'c' which is less than
        word2 again.

        Hence, build the answer char by char, pick from the larger string.

        Note that a non-empty list is greater than an empty list.

        Same as the merge() in 321. Create Maximum Number

        Time: O((A + B) ^ 2) where A is len(word1), B is len(word2)
        Space: O(A + B)
        '''
        A = deque(word1)
        B = deque(word2)

        return "".join(max(A, B).popleft() for _ in range(len(A) + len(B)))