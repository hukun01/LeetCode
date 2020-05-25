# 1456. Maximum Number of Vowels in a Substring of Given Length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''
        Use two pointers to track the vowels count in the
        sliding window of size k.
        Using deque is sub-optimal because of the space cost of storing
        the elements in the deque.
        '''
        v = set('aeiou')
        count = sum(c in v for c in s[:k])
        ans = count
        i1 = 0
        for i2 in range(k, len(s)):
            if s[i2] in v:
                count += 1
            if s[i1] in v:
                count -= 1
            i1 += 1
            ans = max(ans, count)
        return ans