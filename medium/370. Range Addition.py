# 370. Range Addition
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        '''
        Difference array.
        This is the inverse of prefix sums:  diff[i] = nums[i] - nums[i - 1].
        Based on this we know: 
            1. nums[i] = diff[i] + nums[i - 1]
            2. nums[0] = diff[0]
        Then we can get nums by accumulating diff.

        The diff array first collects the start and end positions for each
        udpate interval, and record the delta, by adding `delta` to start,
        and minus `delta` to (end+1). Later we accumulate diff array, the
        `delta` in start will be accumulated to every position after it,
        until (end+1), after which the accumulated `delta` will be negated.

        Difference array provides O(1) update to any intervals in an array,
        with the cost of O(n) query. Hence, this technique is often used in
        scenarios where frequent update operations are applied to various
        intervals, and our goal is to get the result array AFTER all the
        operations.

        Time: O(length)
        Space: O(length)
        '''
        diff = [0] * (length + 1)
        for s, e, inc in updates:
            diff[s] += inc
            diff[e + 1] -= inc
        return list(accumulate(diff[:-1]))