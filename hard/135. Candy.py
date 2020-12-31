# 135. Candy
class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''
        1/2 Greedy.
        Scan the ratings array from left to right, ensure candies[i] has one
        more candy than candies[i-1] if i-th rating is higher.
        Similarly, scan ratings from right to left, ensure candies[i] has one
        more candy than candies[i+1] if i-th rating is higher.

        Time: O(n)
        Space: O(n)
        '''
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)

        '''
        2/2 Array scan.
        When rating is decreasing, increment 'down' that tracks the length of
        decreasing area.
        Keep track of previous highest candies as 'pre'.
        When rating is increasing, if 'down' > 0, add all decreasing area
        to 'total', from 1 back to 'down', which in total is an arithmetic
        progression sum. Note that there can be longer decreasing area, so
        that 'down' >= 'pre', in this case, we need to add 'down - pre + 1'
        more candies, basically to fix 'pre' to be one more than highest bar in
        the 'down' area. Then we can start 'pre' from 1 again.

        Note that if ratings[i-1] == ratings[i], we start 'pre' from 1.
        Also, after iterating the array, if there's 'down' > 0, add its area
        to 'total' and fix the 'pre' as well.

        Time: O(n)
        Space: O(1)
        '''
        if not ratings:
            return 0
        pre = 1
        down = 0
        total = 1
        for i in range(1, len(ratings)):
            if ratings[i-1] > ratings[i]:
                down += 1
                continue

            if down > 0:
                total += down * (down + 1) // 2
                if down >= pre:
                    total += down - pre + 1
                pre = 1
                down = 0

            if ratings[i-1] == ratings[i]:
                pre = 1
            else:
                pre += 1
            total += pre

        if down > 0:
            total += down * (down + 1) // 2
            if down >= pre:
                total += down - pre + 1

        return total