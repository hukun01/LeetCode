class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        Ending with index 'idx', can the string be broken into recognized words.
        '''
        wordDict = set(wordDict)
        cache = { 0: True }
        def check(end):
            if end in cache:
                return cache[end]
            for i in reversed(range(end)):
                if s[i:end] in wordDict and check(i):
                    cache[end] = True
                    return cache[end]
            cache[end] = False
            return cache[end]
        return check(len(s))