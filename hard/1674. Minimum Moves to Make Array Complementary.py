class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        '''
        Difference array.
        Let c be the complementary sum. Different c leads to different
        number of moves, moves[c] = moves[c-1] + diff[c], where diff[c]
        is the difference brought by the c sum.

        Let a, b, c be the nums[i], nums[n - 1 - i], a+b, respectively.
        There are 5 cases that requires different numbers of operations
        to update a and b to get to c, depending on which interval c
        falls in. Assume a <= b:
            1. [2, a], requires 2 ops: change b to 1, a to [1, a-1].
            2. [a+1, a+b), requires 1 op: change b to [1, b-1].
            3. [a+b], requires 0 op.
            4. [a+b+1, b+limit], requires 1 op: change a to [a+1, limit]
            5. [b+limit+1, 2*limit], requires 2 ops: at least need to
               change a to limit, b to b+1.

        Given the intervals of c that adds 0,1,2 ops, our goal is to find
        the interval with the min accumulated ops. It's similar to applying
        +0, +1, +2 update to various intervals in the range of [0, 2*limit],
        and find the smallest update. This is where difference array helps.
        For more about difference array, see 1109. Corporate Flight Bookings.
        Note that the minimum c is 2, so we need to use diff[2:].

        Time: O(max(n, k)) where n is len(nums), k is limit
        Space: O(k)

        Similar to 798. Smallest Rotation with Highest Score.
        '''
        n = len(nums)
        lower_bound = 2
        diff = [0] * (2 * limit + 2)
        for i, a in enumerate(nums[:n//2]):
            b = nums[n - 1 - i]
            if a > b:
                a, b = b, a
            diff[lower_bound] += 2
            # requires 1 less move from 2 moves above, meaning require 1 move.
            diff[a + 1] -= 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            diff[b + limit + 1] += 1
        return min(itertools.accumulate(diff[lower_bound:]))