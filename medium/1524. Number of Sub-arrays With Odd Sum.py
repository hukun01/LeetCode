# 1524. Number of Sub-arrays With Odd Sum
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        '''
        1/2 Prefix sum.
        1. The sum of a subarray [i:j] is prefix[j] - prefix[i].
        2. A odd sum is from (even sum - odd sum) or (odd sum - even sum).
        3. Track the current total prefix sum, and previous sums' odd/even
           counts, if prefix_sum is odd, add the previous even count to ans,
           otherwise, add previous odd count.
        4. Initialize the count with {0:1} to handle first subarray sum being
           odd like [1].

        Time: O(n) where n is len(arr)
        Space: O(1)
        '''
        MOD = 10 ** 9 + 7
        ans = 0
        count = Counter({0: 1})
        prefix_sum = 0
        for a in arr:
            prefix_sum += a
            if prefix_sum % 2 == 1:
                ans += count[0]
            else:
                ans += count[1]
            ans %= MOD
            count[prefix_sum % 2] += 1
        return ans
        '''
        2/2 DP.
        Let f[i] = [x, y], where x is the number of odd sums ending at arr[i-1],
        y is the number of even sums ending at arr[i-1].
        When arr[i-1] is odd:
            f[i][0] = f[i-1][1] + 1, (previous even sums + current, and
            current itself is a new odd sum)
            f[i][1] = f[i-1][0]
        When arr[i-1] is even:
            f[i][0] = f[i-1][0]
            f[i][1] = f[i-1][1] + 1, (previous odd sums + current, and
            current itself is a new even sum)

        Answer is the sum(x[0] for x in f).
        Since f[i] depends on only f[i-1], we can reduce the space usage
        to O(1) by tracking [x, y] only.

        Time: O(n)
        Space: O(1)
        '''
        M = 10 ** 9 + 7
        n = len(arr)
        f = [0, 0] # odd, even
        ans = 0
        for i in range(n):
            a = arr[i]
            f2 = [0, 0]
            if a % 2 == 1:
                f2[0] = f[1] + 1
                f2[1] = f[0]
            else:
                f2[0] = f[0]
                f2[1] = f[1] + 1
            f = f2
            ans += f[0]

        return ans % M