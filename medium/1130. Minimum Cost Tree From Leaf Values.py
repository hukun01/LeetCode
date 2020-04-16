# 1130. Minimum Cost Tree From Leaf Values
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        '''
        Greedy.
        To have the min product from non-leaf node, we need
        to use the min values as the leaves as much as possible.
        In another word, we try to put the bigger numbers as high
        as possible, so they have a smaller impact to the final result.

        TODO: explore the O(n) time/space solution based on monotic stack.
        '''
        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            res += min(arr[i - 1: i] + arr[i + 1: i + 2]) * arr.pop(i)
        return res