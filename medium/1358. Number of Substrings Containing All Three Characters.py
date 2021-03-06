# 1358. Number of Substrings Containing All Three Characters
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        '''
        1/2 Sliding window.
        At each index i, we count all the substrings that *end* at s[i], as
        long as they contain at least one of each characters.
        Use a sliding window to find the shortest substring that satisfies and
        ends at s[i]. Each previous index p to the window's left, can form a
        good substring with s[p: i+1], totally, there are (left + 1) such
        substrings.

        Time: O(n) where n is len(s)
        Space: O(1)
        '''
        ans = 0
        counts = Counter()
        left = 0
        need = 3
        for char in s:
            if char not in counts:
                need -= 1
            counts[char] += 1
            if need == 0:
                while counts[s[left]] > 1:
                    counts[s[left]] -= 1
                    left += 1
                ans += left + 1
        return ans
        '''
        2/2 Sliding window, different style.
        Record the last index of each element.
        A substring is defined by [startIdx, i]. At each index i, we find
        the number of startIdx, which will be the number of substrings.
        The range of startIdx is [0, min(last.values())], with last initialized
        with -1 for each element. Defaults will cover the scenarios when we
        haven't find all elements yet.
        Hence the number of substrings is 1 + min(last.values()).
        '''
        last = { 'a': -1, 'b': -1, 'c': -1 }
        ans = 0
        for i, c in enumerate(s):
            last[c] = i
            ans += 1 + min(last.values())
        return ans