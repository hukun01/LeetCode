class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        '''
        Sliding window.
        
        Let allowed = aeiou
        Whennever i see x that is the i-th char in allowed, the next one is either
        i-th or (i+1)-th char.
        If it's something else, i would reset and start the new process from there.

        We can keep adding c to seen without checking whether c == 'a', because if
        c != 'a', we will never hit len(seen) == 5. Due to the `word[i] < word[i-1]`
        condition, we only reach len(seen) == 5 when the whole substring is increasing.
        '''
        ans = 0
        start = 0
        seen = set()
        for i, c in enumerate(word):
            if i > 0 and word[i] < word[i-1]:
                seen = set()
                start = i
            seen.add(c)
            if len(seen) == 5:
                ans = max(ans, i - start + 1)
        return ans
