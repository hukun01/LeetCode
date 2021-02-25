# 1769. Minimum Number of Operations to Move All Balls to Each Box
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        '''
        DP.
        At each index i, the ops needed to move all balls to the left of i,
        is the accumulated balls count from each position. The 'cur' is the
        total balls. The 'steps' is the total ops needed to move all balls we
        get so far to the next position.

        Time: O(n)
        Space: O(n)
        '''
        n = len(boxes)
        ans = [0] * n
        cur = steps = 0
        for i in range(n):
            ans[i] += steps
            cur += int(boxes[i])
            steps += cur

        cur = steps = 0
        for i in reversed(range(n)):
            ans[i] += steps
            cur += int(boxes[i])
            steps += cur

        return ans