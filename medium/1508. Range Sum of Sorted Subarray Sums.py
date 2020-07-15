# 1508. Range Sum of Sorted Subarray Sums
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        '''
        1/2 Naive.
        O(n^2 logn) time, O(n^2) space.
        '''
        sums = sorted(itertools.chain(
            *(itertools.accumulate(nums[i:]) for i in range(len(nums)))))
        return sum(sums[left-1: right]) % int(1e9+7)
    
        '''
        2/2 Track the range sums as a list of linked lists head.
        Use a heap to track the range sums and their tail positions.
        The initial range sums are just each element and index.
        As the step increments, heap pop the (smallest range sum, tail position),
        if step >= left, add the range sum to answer, and update heap
        to add the new range sum based on the current range sum and the next
        element after tail.
        O(n^2 logn) time, O(n) space.
        '''
        h = [(x, i) for i, x in enumerate(nums)]
        heapify(h)
        
        ans = 0
        for k in range(1, right+1):
            x, i = heappop(h)
            if k >= left: ans += x
            if i+1 < len(nums): 
                heappush(h, (x + nums[i+1], i+1))
                
        return ans % int(1e9+7)