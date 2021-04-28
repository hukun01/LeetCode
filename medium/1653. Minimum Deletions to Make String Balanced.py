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
        left_b + (total_a - left_a).

        Time: O(n) where n is the length of s.
        Space: O(1)
        '''
        total_a = sum(c == 'a' for c in s)
        seen = Counter()
        ans = total_a
        for c in s:
            seen[c] += 1
            left_b = seen['b']
            right_a = total_a - seen['a']
            ans = min(ans, left_b + right_a)

        return ans