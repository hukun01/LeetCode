# 1888. Minimum Number of Flips to Make the Binary String Alternating
class Solution:
    def minFlips(self, s: str) -> int:
        '''
        1/2 Sliding window + replicate string.

        When we can move elements from head to tail, think about replicating
        the string using s += s, and apply sliding window. This way, we use the
        sliding window to process the s + s in linear time, and consider all
        possible cases of head-to-tail elements.

        In this new s+s, we can find the minimum flips needed by tracking the
        sliding window diffs comparing to the 2 expected results.

        Time: O(n) where n is len(s)
        Space: O(n)
        '''
        n = len(s)
        s += s
        s1 = []
        s2 = []
        for i, c in enumerate(s):
            if i % 2 == 0:
                s1.append('1')
                s2.append('0')
            else:
                s1.append('0')
                s2.append('1')

        a1 = 0
        a2 = 0
        ans = inf
        for i in range(len(s)):
            if s1[i] != s[i]:
                a1 += 1
            if s2[i] != s[i]:
                a2 += 1
            if i >= n:
                if s1[i-n] != s[i]:
                    a1 -= 1
                if s2[i-n] != s[i]:
                    a2 -= 1
            if i >= n - 1:
                ans = min(ans, a1, a2)

        return ans
        '''
        2/2 Same idea, constant space.

        Notice that we don't really need to generate the whole expected
        strings to compare, as the char on each index is known.
        Also, we don't need to literally replicate the string, but just need
        to iterate through the index twice.
        '''
        n = len(s)
        a1 = 0
        a2 = 0
        ans = inf
        for i in range(n * 2):
            c1 = str(1 - i % 2)
            c2 = str(i % 2)
            if c1 != s[i % n]:
                a1 += 1
            if c2 != s[i % n]:
                a2 += 1
            if i >= n:
                if str(1 - (i-n) % 2) != s[i % n]:
                    a1 -= 1
                if str((i-n) % 2) != s[i % n]:
                    a2 -= 1
            if i >= n - 1:
                ans = min(ans, a1, a2)

        return ans