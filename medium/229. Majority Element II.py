# 229. Majority Element II
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        Math.
        Note that there can be at most 2 numbers that appear more than n//3
        times. Thus, we can use an updated version of voting algorithm, with
        2 candidates representing the most frequent values.
        Then we verify them to confirm their majority.
        This can be extended to x in which we look for numbers that appear
        more than n // x times.
        Similar to 169. Majority Element.
        '''
        candidate1 = candidate2 = None
        vote1 = vote2 = 0
        for a in nums:
            if candidate1 == a:
                vote1 += 1
            elif candidate2 == a:
                vote2 += 1
            elif vote1 == 0:
                candidate1 = a
                vote1 += 1
            elif vote2 == 0:
                candidate2 = a
                vote2 += 1
            else:
                vote1 -= 1
                vote2 -= 1
        ans = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums) // 3:
                ans.append(c)
        return ans