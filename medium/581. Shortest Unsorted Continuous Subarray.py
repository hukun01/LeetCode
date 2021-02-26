# 581. Shortest Unsorted Continuous Subarray
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        '''
        1/2 Mono stack.
        An easier way is to sort the array and find the mismatched points, but
        that takes O(n log(n)) time.
        We can leverage the expectation that the array should be increasing.
        Using a stack to track the increasing values, when seeing a smaller
        value, then there's an unsorted area, we start poping out the index in
        stack, until some previous index has smaller value than the current
        value. And we pick the smallest index as the left boundary.
        Similarly, reversely traverse the array, and find the right boundary.

        Time: O(n) where n is len(nums)
        Space: O(n)
        '''
        stack = []
        n = len(nums)
        l = n
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)

        r = 0
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)

        return max(0, r - l + 1)
        '''
        2/2 Optimized using constant space.
        Similar idea as 1/2, but here we don't store all visited values in
        stack, but just record the max so far, and record the last index that
        has smaller value than the max, this is the end of unsorted subarray.
        Similarly, reversely, record the min so far, and record the last index
        that has bigger value than the min, this is the start of unsorted.

        Time: O(n)
        Space: O(1)
        '''
        n = len(nums)
        min_val = inf
        max_val = -inf
        start = 0
        end = -1
        for i in range(n):
            if nums[i] >= max_val:
                max_val = nums[i]
            else:
                end = i

        for i in range(n-1, -1, -1):
            if nums[i] <= min_val:
                min_val = nums[i]
            else:
                start = i

        return end - start + 1