# 1537. Get the Maximum Score
class Solution:
    def maxSum(self, A: List[int], B: List[int]) -> int:
        '''
        Greedy.
        Imagine the 2 arrays are 2 linked lists, and 2 lists interleaves
        at the common values.
        If there's any common value, we can only select one of the
        two paths with the greater sum. Same applies to the path segment
        between common values.
        Keep track of the sums for the two paths a and b, and move
        the step in the array with smaller value, because we don't want
        to miss the (i, j) position where A[i] == B[j]. Once A[i] == B[j],
        add the greater path sum to 'ans', and reset a and b.
        After one path exhaust, add the rest of other array, and add the
        max(a, b) to 'ans'.

        Note that when comparing sums with MOD, we should do MOD to
        the final answer, but not to the intermediate results. For example,
        say MOD = 107, (100 % MOD) > (110 % MOD), even though 100 < 110.
        '''
        ans = a = b = 0
        i = j = 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                a += A[i]
                i += 1
            elif A[i] > B[j]:
                b += B[j]
                j += 1
            else:
                ans += max(a, b) + A[i]
                a = b = 0
                i += 1
                j += 1
        a += sum(A[i:])
        b += sum(B[j:])
        ans += max(a, b)
        return ans % (10 **9 + 7)