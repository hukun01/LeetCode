class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # use two inner loop to handle vertical row and oblique row
        # we use the first (numRows) chars to build the first (numRows) rows;
        # we use the (numRows+x)th char for the (numRows-2-x)th row, x in [0, numRows-2)
        i = 0
        ans = [[] for _ in range(numRows)]
        while i < len(s):
            for j in range(min(numRows, len(s) - i)):
                ans[j].append(s[i])
                i += 1
            for j in range(min(numRows - 2, len(s) - i)):
                ans[numRows - 2 - j].append(s[i])
                i += 1
            
        return "".join(char for row in ans for char in row)