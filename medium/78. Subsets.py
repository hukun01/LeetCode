# 78. Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = [[]]
        for n in nums:
            next_level = curr[:]
            for s in curr:
                next_level.append(s + [n])
            curr = next_level
        return curr