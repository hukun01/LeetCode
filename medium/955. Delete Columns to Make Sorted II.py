# 955. Delete Columns to Make Sorted II
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        '''
        Greedy.
        The key is to continue processing the rows whose previous columns have
        the same value. For example, ["ax", "ay", "bx"], after processing the
        first column, the data for effective validation becomes ["x", "y"].
        We use prev_col_sorted_from_row[i] = True, to represent that the row i
        and i+1 are already sorted based on their previous column values, so
        we don't care if current col[i] <= col[i+1] or not.
        We set this flag to True whenever col[i] < col[i+1].

        Time: O(n w) where n is len(A), w is len(A[0])
        Space: O(n)
        '''
        n = len(A)
        prev_col_sorted_from_row = [False] * (n - 1)

        ans = 0
        for col in zip(*A):
            if all(prev_col_sorted_from_row[i] or col[i] <= col[i + 1]
                    for i in range(len(col) - 1)):
                for i in range(len(col) - 1):
                    if col[i] < col[i + 1]:
                        prev_col_sorted_from_row[i] = True
            else:
                ans += 1

        return ans