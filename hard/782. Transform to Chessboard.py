# 782. Transform to Chessboard
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        '''
        1/2 Array with O(1) space.

        Two steps in general.
        1. Check whether this is possible to transform.
            Make two checks and if both pass, we are sure that this board can
            transform:
            1. A good starting board has exactly two kinds of rows, and these
            two rows must negate each other. Same applies column wise. This
            means that the 4 corners of any rectangle in the board must be 4
            ones, or 4 zeros, or 2 ones and 2 zeros, otherwise this board can't
            transform to chessboard.
            2. After the first check we know there are exactly two kinds of
            rows and one row is the inversed version of another. Now we just
            need to check the first row, or any row that: if the number of ones
            in this row is not n / 2 or (n + 1) / 2, then the column swaps
            would never lead to chessboard. Same applies column wise.
        2. Count the total number X of misplaced cells in a row and in a col,
        the number of swaps needed will be X / 2.

        The key is to do step 1. There are other simpler ways to perform the
        two checks by Counter(), but will require O(n) space.

        Time: O(n^2)
        Space: O(1)
        '''
        b = board
        n = len(b)
        if any(b[0][0] ^ b[i][0] ^ b[0][j] ^ b[i][j] for i in range(n) for j in range(n)):
            return -1
        if not n // 2 <= sum(b[0]) <= (n + 1) // 2:
            return -1
        if not n // 2 <= sum(b[i][0] for i in range(n)) <= (n + 1) // 2:
            return -1

         # Number of properly placed cells in the row, can be treated as
         # misplaced cells as well. Similar for colums.
        row_sum = sum(b[0][i] == i % 2 for i in range(n))
        col_sum = sum(b[i][0] == i % 2 for i in range(n))

        if n % 2 == 1:
            if row_sum % 2 == 1:
                # When n is odd, if the number of properly placed rows is odd,
                # then the misplaced rows must be even, so we have to
                # touch even number of rows. Same applies to cols.
                row_sum = n - row_sum
            if col_sum % 2 == 1:
                col_sum = n - col_sum
        else:
            row_sum = min(n - row_sum, row_sum)
            col_sum = min(n - col_sum, col_sum)
        return (col_sum + row_sum) // 2
        '''
        2/2 Array. Same idea as 1/2, but with simpler checks implementation,
        and use O(n) space.
        '''
        b = board
        n = len(b)

        row_counts = Counter()
        for r in b:
            row_counts[''.join([str(c) for c in r])] += 1
        if len(row_counts) != 2:
            return -1
        r1, r2 = row_counts.keys()
        if any(a == b for a, b in zip(r1, r2)) or \
                abs(r1.count('0') - r2.count('0')) > 1 or \
                not n // 2 <= r1.count('0') <= (n + 1) // 2:
            return -1

        row_sum = sum(b[0][i] == i % 2 for i in range(n))
        col_sum = sum(b[i][0] == i % 2 for i in range(n))

        if n % 2 == 1:
            if row_sum % 2 == 1:
                row_sum = n - row_sum
            if col_sum % 2 == 1:
                col_sum = n - col_sum
        else:
            row_sum = min(n - row_sum, row_sum)
            col_sum = min(n - col_sum, col_sum)
        return (col_sum + row_sum) // 2