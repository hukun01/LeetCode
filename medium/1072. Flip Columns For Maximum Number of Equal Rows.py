class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        '''
        The key is to count the number of 'pattern' of each row, if 2 rows have the same 0/1 pattern,
        any number of their columns can be flipped to make them uni-value.
        '''
        counter = Counter()
        for row in matrix:
            pattern = tuple(col ^ row[0] for col in row)
            counter[pattern] += 1
        return max(counter.values())