class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        This problem is an extension of twoSum problem. We sort the array to ensure that
        triplets are internally ordered. And in each iteration, we take the current number,
        and find the twoSum tuples from the rest of the array.
        Also need to dedup before using the current number.
        '''
        nums.sort()
        answers = set()
        for i, n in enumerate(nums[:-2]):
            if i >= 1 and n == nums[i - 1]:
                continue
            seen = set()
            for x in nums[i+1:]:
                if (-n-x) in seen:
                    # (-n-x) falls into [n, x]
                    answers.add((n, -n-x, x))
                seen.add(x)
        return list(map(list, answers))