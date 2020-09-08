# 1297. Maximum Number of Occurrences of a Substring
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        '''
        Observation.
        For any substring, if it appears x times, its substrings must appear
        at least x times. In another word, the substrings with minSize must
        be the most frequent ones. To find the max frequency, we only need to
        look at minSize.
        '''
        k = minSize
        count = Counter(s[i:i + k] for i in range(len(s) - k + 1))
        return max([count[w] for w in count if len(set(w)) <= maxLetters], default=0)