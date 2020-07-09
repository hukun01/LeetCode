# 15. 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        This problem is an extension of twoSum problem. We sort the array to ensure that
        triplets are internally ordered. And in each iteration, we take the current number,
        and find the twoSum tuples from the rest of the array.
        Also need to dedup before using the current number.
        '''
        nums.sort()
        answer = set()
        for i, a in enumerate(nums[:-2]):
            if i-1 >= 0 and a == nums[i-1]:
                continue
            seen = set()
            for c in nums[i+1:]:
                b = 0 - a - c # b will fall into [a, c] if b can be part of an answer
                if b in seen:
                    answer.add((a, b, c))
                seen.add(c)
        return [list(triplet) for triplet in answer]
        '''
        Another style.
        '''
        nums.sort()
        ans = []
        for l in range(len(nums) - 2):
            if l - 1 >= 0 and nums[l - 1] == nums[l]:
                continue
            m = l + 1
            r = len(nums) - 1
            while m < r:
                total = nums[l] + nums[m] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    m += 1
                else:
                    ans.append([nums[l], nums[m], nums[r]])
                    while m + 1 <= r and nums[m] == nums[m + 1]:
                        m += 1
                    while r - 1 >= m and nums[r] == nums[r - 1]:
                        r -= 1
                    m += 1
                    r -= 1
        return ans