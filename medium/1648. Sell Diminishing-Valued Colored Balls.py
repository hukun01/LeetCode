# 1648. Sell Diminishing-Valued Colored Balls
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        '''
        1/2 Sort.
        We sort the frequencies of inventory then sort it reversely, and we
        take from the largest counts in batches.
        A corner case is when we have less order than the batch. In this case,
        we need to count the 'whole' - the count value which we would take all
        from the batch. And we take one ball from 'remainder' counts, note that
        each ball has value 'count - whole'.

        Note that a [(0, 0)] is added to the end so we never go out of bound.

        Time: O(n log(n)) where n is len(inventory)
        Space: O(n)
        '''
        arr = sorted(Counter(inventory).items(), reverse=True) + [(0, 0)]
        ans, idx, width = 0, 0, 0

        while orders > 0:
            count, freq = arr[idx]
            width += freq
            next_count = arr[idx + 1][0]
            sell = min(orders, width * (count - next_count))
            whole, remainder = divmod(sell, width)
            ans += width * whole * (count + count - whole + 1) // 2 + remainder * (count - whole)
            orders -= sell
            idx += 1
        return ans % 1_000_000_007

        '''
        2/2 Binary search.
        We need to find a T where we take the last T from some i's,
        and take the last (T - 1) from some other i's. And we have
        ∑_(i >= T)(i - T) <= orders <= ∑_(i >= T)(i - T + 1)
        Let extra = orders - ∑_(i >= T)(i - T), this is the number
        of i's where we need to take the last T, it can be any i's
        that are >= T.

        An example is [2, 3, 3], 6
        1,2
        1,2,3
        1,2,3
        Then T is 1, and extra is 1, so we can take as below.
        1,2    take [1,2]
        1,2,3  take [2,3]
        1,2,3  take [2,3]

        Time: O(NlogM) where N is len(inventory), M is the max of it.
        Space: O(1).
        '''
        mod = 10**9 + 7

        l, r = 0, max(inventory)
        while l < r:
            mid = (l + r) // 2
            total = sum(i - mid for i in inventory if i >= mid)
            if total <= orders:
                r = mid
            else:
                l = mid + 1
        T = l
        range_sum = lambda s, e: (s + e) * (e - s + 1) // 2

        extra = orders - sum(i - T for i in inventory if i >= T)
        ans = 0
        for i in inventory:
            if i < T:
                continue
            if extra > 0:
                ans += range_sum(T, i)
                extra -= 1
            else:
                ans += range_sum(T + 1, i)

        return ans % mod