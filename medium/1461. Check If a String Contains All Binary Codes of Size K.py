# 1461. Check If a String Contains All Binary Codes of Size K
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        '''
        1/2 Sliding window and set
        Use a sliding window to capture all the possible substrings with
        length k, and check whether the size of the set is 2 ** k.
        '''
        allCodes = set()
        for i in range(k, len(s) + 1):
            allCodes.add(s[i-k: i])
        return len(allCodes) == 2 ** k
        '''
        2/2 Sliding window and array
        Use an array with size (2 ** k), and convert each substring into integer,
        which is the index in the array, then make sure all elements in the array
        is set.
        '''
        codes = [0] * (2**k)
        for i in range(k, len(s) + 1):
            codes[int(s[i-k: i], 2)] = 1
        return all(c == 1 for c in codes)