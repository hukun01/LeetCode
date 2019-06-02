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
            if i > 0 and nums[i] == nums[i-1]:
                continue
            seen = set()
            for c in nums[i+1:]:
                b = 0 - a - c # b will fall into [a, c] if b can be part of an answer
                if b in seen:
                    answer.add((a, b, c))
                seen.add(c)
        return list(map(list, answer))