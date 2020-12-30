# 6. ZigZag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        Use two inner loop to handle vertical row and oblique row.
        Use the first (numRows) chars to build the first (numRows) rows;
        Use the (numRows+x)th char for the (numRows-2-x)th row, x in [0, numRows-2)

        Time: O(n) where n is len(s)
        Space: O(n)
        '''
        i = 0
        rows = [[] for _ in range(numRows)]
        n = len(s)
        while i < n:
            for r in range(min(numRows, n - i)):
                rows[r].append(s[i])
                i += 1
            for j in range(min(numRows - 2, n - i)):
                rows[numRows - 2 - j].append(s[i])
                i += 1

        return ''.join(char for row in rows for char in row)