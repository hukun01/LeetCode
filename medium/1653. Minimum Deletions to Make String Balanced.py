# 1653. Minimum Deletions to Make String Balanced
class Solution:
    def minimumDeletions(self, s: str) -> int:
        '''
        Array.
        At each position of s, we need to delete all 'b' on the left, and all
        'a' on the right. We can iterate through each position, and find the
        min deletion.
        To get the deletion count efficiently, count the total number of 'a'.
        Then at each position, the deletion count will be
        left_b + (num_a - left_a).

        Time: O(n) where n is the length of s.
        Space: O(1)
        '''
        num_a = sum(c == 'a' for c in s)
        freq = Counter()
        ans = freq['b'] + num_a - freq['a']
        for c in s:
            freq[c] += 1
            ans = min(ans, freq['b'] + num_a - freq['a'])

        return ans