# 1130. Minimum Cost Tree From Leaf Values
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        '''
        1/2 Greedy.

        Each time we use two leaves, the smaller leaf wouldn't get used
        anymore, so essentially we pay a*b cost to remove 'a', where 'a <= b'.

        To have the min product from non-leaf node, we need to use the min
        values as the leaves as early as possible. In another word, we try to
        put the bigger numbers as high as possible, so they have a smaller
        impact to the final result.

        Until arr gets to one element, we find the min element 'a' in each
        iteration, and to use it, we find the smaller one of the greater
        neighbors from left and right, this is the 'b'. Now we add 'a*b', and
        pop(a).

        Time: O(n^2) where n is len(arr), we need O(n) time to iterate, in each
              iteration, we use another O(n) time to find and remove 'a'.
        Space: O(n)

        TODO: explore the O(n) time/space solution based on monotic stack.
        '''
        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            res += min(arr[i - 1: i] + arr[i + 1: i + 2]) * arr.pop(i)
        return res
        '''
        2/2 Monotonic stack.
        '''