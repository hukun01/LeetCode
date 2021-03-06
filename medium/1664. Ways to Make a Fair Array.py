# 1664. Ways to Make a Fair Array
class Solution:
    def waysToMakeFair(self, A: List[int]) -> int:
        '''
        Sliding split.
        Let s1 record the even and odd sums on the left;
        Let s2 record the even and odd sums on the right.

        Time: O(N) where N is len(A).
        Space: O(1).
        '''
        s1, s2 = [0, 0], [sum(A[0::2]), sum(A[1::2])]
        ans = 0
        for i, a in enumerate(A):
            s2[i % 2] -= a
            if s1[0] + s2[1] == s1[1] + s2[0]:
                ans += 1
            s1[i % 2] += a

        return ans