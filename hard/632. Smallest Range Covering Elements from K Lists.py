# 632. Smallest Range Covering Elements from K Lists
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        '''
        Priority queue + sliding window.

        Record the left positions in a heap, similar to merge k sorted list,
        so we can keep track of the left boundaries as we move the sliding
        window. And we just need to record the right position in one variable,
        and keep updating it when window moves.
        We exit the loop when any list runs out.
        Key is to initialize the right val as the max of all the first element
        in each list.

        Time: O(nk log(k)) where n is length of a single list, k is number of
              lists.
        Space: O(k)
        '''
        left_pos = [(a[0], i, 0) for i, a in enumerate(nums)]
        heapify(left_pos)
        ans = [-1e5, 1e5]
        right = max(a[0] for a in nums)
        while left_pos:
            left, list_i, left_i = heappop(left_pos)
            if right - left < ans[1] - ans[0]:
                ans = [left, right]
            if left_i + 1 == len(nums[list_i]):
                break
            new_val_from_list_i = nums[list_i][left_i + 1]
            right = max(right, new_val_from_list_i)
            heappush(left_pos, (new_val_from_list_i, list_i, left_i + 1))
        return ans