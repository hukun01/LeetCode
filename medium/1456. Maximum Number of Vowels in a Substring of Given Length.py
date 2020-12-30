# 1456. Maximum Number of Vowels in a Substring of Given Length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''
        Sliding window.
        Use two pointers to track vowels count in the sliding window of size k.
        Note that using a deque is sub-optimal because of the space cost.

        Time: O(n) where n is len(s)
        Space: O(1)
        '''
        vowels = set('aeiou')
        cur = left = ans = 0
        for right, char in enumerate(s):
            cur += int(char in vowels)
            while right - left + 1 > k:
                cur -= int(s[left] in vowels)
                left += 1
            ans = max(ans, cur)
        return ans