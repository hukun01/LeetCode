# 1072. Flip Columns For Maximum Number of Equal Rows
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        '''
        Hashmap.
        The key is to count the number of 'pattern' of each row, if 2 rows have
        the same 0/1 pattern, any number of their columns can be flipped to
        make them uni-value.

        Time: O(RC) where R is len(matrix), C is len(matrix[0])
        Space: O(RC)
        '''
        counter = Counter()
        for row in matrix:
            pattern = tuple(col ^ row[0] for col in row)
            counter[pattern] += 1
        return max(counter.values())