class Solution:
    def customSortString(self, S: str, T: str) -> str:
        '''
        Get familiar with counter.items() and counter.pop(key) to remove a key. 
        Also notice that if T has a character that appears more than once, 
        they all need to be in the same order as the single character appears in S.
        '''
        counter = collections.Counter(T)
        answer = []
        for c in S:
            if c in counter:
                answer.append(c * counter[c])
                counter.pop(c)
        for c, v in counter.items():
            answer.append(c * v)
        return ''.join(answer)