# 398. Random Pick Index
class Solution:
    '''
    Reservoir sampling.

    Time: O(n) where n is len(nums).
    Space: O(1)

    Same as 382. Linked List Random Node
    '''
    def __init__(self, nums: List[int]):
        self.data = nums

    def pick(self, target: int) -> int:
        counter = 0
        ans = 0
        for i, n in enumerate(self.data):
            if n == target:
                counter += 1
                if random.randrange(counter) == 0:
                    ans = i
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)