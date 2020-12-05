# 1103. Distribute Candies to People
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        '''
        Math.
        Simulation method is trivial and takes O(sqrt(candies)) time,
        here is the math solution that takes O(n) time.
        Let x be the count of complete gifts, which is also the last/biggest
        number of gifts we have even given. Then we have
        candies >= x * (1+x) / 2 > x*x / 2, so sqrt(2 * candies) > x,
        note that int((2 * candies) ** 0.5) is in range [x, x+1], so
        need to double check in case it's x+1 instead of x.

        Once we get x, we can list the complete gifts as a matrix, and
        we know the rows and cols and leftover partial gift.
        Now we can get the total gift for each people in O(1) time.
        '''
        n = num_people
        ans = [0] * n
        gifts_count = int((candies * 2) ** 0.5)
        if gifts_count * (1 + gifts_count) // 2 > candies:
            gifts_count -= 1
        rows = gifts_count // n
        cols = gifts_count % n
        remain = candies - gifts_count * (1 + gifts_count) // 2
        for i in range(n):
            ans[i] = n * rows * (rows - 1) // 2 + (i + 1) * rows
            if i < cols:
                ans[i] += i + 1 + rows * n
        ans[cols] += remain
        return ans