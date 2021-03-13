# 1674. Minimum Moves to Make Array Complementary
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        '''
        1/3 Difference array.
        Let c be the complementary sum. Different c leads to different
        number of moves. Let moves[c] be the number of total moves to reach c.

        Let a, b, c be the nums[i], nums[n - 1 - i], a+b, respectively.
        There are 5 cases that requires different numbers of operations
        to update a and/or b to get to c, depending on which interval c
        falls in. Assume a <= b:
            1. [2, a], requires 2 ops: change b to 1, a to [1, a-1].
            2. [a+1, a+b), requires 1 op: change b to [1, b-1].
            3. [a+b], requires 0 op.
            4. [a+b+1, b+limit], requires 1 op: change a to [a+1, limit]
            5. [b+limit+1, 2*limit], requires 2 ops: at least need to
               change a to limit, b to b+1.

        Given the intervals of c that adds 0, 1, 2 ops, our goal is to find
        the point with the min accumulated ops. It's similar to applying
        +0, +1, +2 update to various intervals in the range of [0, 2*limit],
        each interval is updated up to n times. Then find the smallest updated
        point after all updates are done.

        We can update moves[c] for every A[i], by adding corresponding update
        to the above 5 intervals, but it's O(n*k) time. When we do frequent
        updates to various intervals, and get the final result, it is where
        difference array helps, because it supports O(1) update and O(n) query.
        Let moves[c] = moves[c-1] + diff[c], where diff[c] is the difference
        brought by the updating from (c-1) to c.
        Note that the minimum c is 2, so we need to use diff[2:].

        Time: O(max(n, k)) where n is len(nums), k is limit
        Space: O(k)

        Similar to 798. Smallest Rotation with Highest Score.
        '''
        n = len(nums)
        lower_bound = 2
        diff = [0] * (2 * limit + 2)
        for i in range(n // 2):
            a, b = sorted([nums[i], nums[n - 1 - i]])

            diff[lower_bound] += 2
            # below line is the shortcut to diff[a+1] -= 2 and diff[a+1] += 1.
            diff[a + 1] -= 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            diff[b + limit + 1] += 1
        return min(accumulate(diff[lower_bound:]))
        '''
        2/3 Binary search.
        Assume in each pair (a, b), a <= b. Similar to logic in 1/3, we have:
        If target is t, then
            limit + b < t, we need to increase both numbers, 2 ops
            a + 1 > t, we need to decrease both numbers, 2 ops
            a + b == t, we don't do anything, 0 ops
            the other cases, we need to do one operation, 1 ops
        We iterate through all possible targets, in [2, 2 * limit + 1].
        For each target t, we find:
            the number of pairs that sum to t;
            the number of pairs that need 2 increase ops;
            the number of pairs that need 2 decrease ops;
            the number of pairs that need 1 (inc/dec) ops is n - t.
        Note that n is the number of pairs = len(nums) // 2, not len(nums).
        
        Use binary search to find increase_both and decrease_both. For example,
        for increase_both, we can find from b's list the number of elements
        that are < t - limit.

        Then the total ops = n - equal + increase_both + decrease_both,
        note that (n - equal) includes the number of pairs that need 2 ops, so
        we just add the 'increase_both' and 'decrease_both' once again.

        Time: O(k log(n) + n log(n))
        Space: O(n)
        '''
        n = len(nums) // 2
        pairs = [(a, b) for a, b in zip(nums[:n], nums[n:][::-1])]
        bbs = sorted(max(a, b) for a, b in pairs)
        aas = sorted(min(a, b) for a, b in pairs)
        sums = Counter(a + b for a, b in pairs)
        ans = sys.maxsize
        for t in range(2, limit * 2 + 1):
            equal = sums[t]
            increase_both = bisect_left(bbs, t - limit)
            decrease_both = n - bisect_left(aas, t)
            ans = min(ans, n - equal + increase_both + decrease_both)
        return ans
        '''
        3/3 Events and line sweep.
        The difference array technique is nice, but it would be constrained if
        the values are huge. In that case, we need a scalable approach that
        doesn't concern about the actual values.

        Similar to logic in 1/3, but opposite, based on below:
        There are 5 cases that requires different numbers of operations
        to update a and/or b to get to c, depending on which interval c
        falls in. Assume a <= b:
            1. [2, a], requires 2 ops: change b to 1, a to [1, a-1].
            2. [a+1, a+b), requires 1 op: change b to [1, b-1].
            3. [a+b], requires 0 op.
            4. [a+b+1, b+limit], requires 1 op: change a to [a+1, limit]
            5. [b+limit+1, 2*limit], requires 2 ops: at least need to
               change a to limit, b to b+1.

        Instead of looking for min ops, we look for max number of elements that
        stay the same. Then we have the opposite cases:
            1. [a+1, a+b), 1 number stays the same, +1
            2. [a+b], 1 more number stays the same, +1
            3. [a+b+1, b+limit], 1 less number stays the same, -1
            4. [b+limit+1, 2*limit), 1 less number stays the same, -1
        We can do the same difference array technique as in 1/3 to find the max
        number of elements that stay the same.
        
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        for i in range(n // 2):
            a, b = sorted([nums[i], nums[n - 1 - i]])

            diff[a+1] += 1
            diff[a+b] += 1
            diff[a+b+1] -= 1
            diff[b+limit+1] -= 1

        return n - max(accumulate(diff))

        Alternatively, we can collect those change points as events, and do
        line sweep to find the same answer. The advantage of the second
        solution is that it doesn't depend on the value of limit.

        Time: O(n log n)
        Space: O(n)
        '''
        n = len(nums)
        events = []
        for i in range(n // 2):
            a, b = sorted([nums[i], nums[n - 1 - i]])

            events.append((a + 1, 1))
            events.append((a + b, 1))
            events.append((a + b + 1, -1))
            events.append((b + limit + 1, -1))

        events.sort()
        return n - max(accumulate(delta for _, delta in events))