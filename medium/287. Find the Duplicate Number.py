# 287. Find the Duplicate Number
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        2 solutions:
        1/2. Linked list - from the index to value mappings, there must be a cycle.
        Find the cycle entry point in a linked list
        The key here is to start from 0, because no nodes can reach node 0 once we start.
        Other cycle might exist, but Node 0 will not reach them, because nums is from [1, n].
        Another form of this problem is that nums is from [0, n-1], in which we should start
        searching from Node len(nums) - 1.
        """
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow

        """
        2/2. Binary search:
        search space: [1, n]
        predicate: For a number X in nums, if the count of {numbers < X} is
        greater than X, then the duplicate number must be less than X.

        def count(nums, target):
            return sum([1 if n <= target else 0 for n in nums])
        
        l, h = 1, len(nums) - 1
        while l < h:
            m = (l + h) // 2
            if count(nums, m) <= m:
                l = m + 1
            else: # count > m
                h = m
        return l
        """