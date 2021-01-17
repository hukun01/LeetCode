# 1524. Number of Sub-arrays With Odd Sum
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        '''
        Prefix sum.
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