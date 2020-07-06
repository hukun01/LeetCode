# 1504. Count Submatrices With All Ones
class Solution:
    '''
    Reduce 2D array to 1D.
    For each row, record the height at each column, and count the number
    of submatrices whose right border is the current column.
    Use a monotically increasing stack to track the heights, when seeing
    a lower height h, pop out all the recent higher ones in the stack, so
    to form submatricies whose right border is h. The number of such
    submatricies is equal to the area of the largest submatricies that can
    be formed with h.

    Similar to 84. Largest Rectangle in Histogram.
    '''
    def numSubmat(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])
        def count(heights):
            previous_idx = []
            totals = [0] * (len(heights))
            for i, h in enumerate(heights):
                while previous_idx and heights[previous_idx[-1]] >= h:
                    previous_idx.pop()
                    
                if previous_idx:
                    prev_i = previous_idx[-1]
                    totals[i] = totals[prev_i]
                    totals[i] += h * (i - prev_i)
                else:
                    totals[i] = h * (i + 1)
                
                previous_idx.append(i)
                
            return sum(totals)
        
        row = [0] * C
        ans = 0
        for r in range(R):
            for c in range(C):
                row[c] = row[c] + 1 if mat[r][c] == 1 else 0
            ans += count(row)
        return ans