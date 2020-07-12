# 1424. Diagonal Traverse II
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        '''
        Note that for every number, its position (row, col), row + col
        maps to its final access order, reversely.
        We can just collect the numbers in a list for every order, and process
        them at the end.
        Another approach is to do BFS.
        '''
        ans = defaultdict(list)
        upper = 0
        for r in range(len(nums)):
            for c, x in enumerate(nums[r]):
                ans[c + i].append(x)
            upper = max(upper, i + len(nums[r]) - 1)
        res = []
        for x in range(upper + 1):
            res += ans[x][::-1]
        return res