# 456. 132 Pattern
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        '''
        Stack.
        Reverse the input array, so our target transforms to:
        finding 231 pattern.
        For each number n, we find the number '2', s3, in the 231 pattern,
        which is the biggest number that's smaller than n, by using a
        monotonically decreasing stack.
        Now we have s3 < last_n, if any curr_n < s3, then we have the 231 pattern.
        '''
        stack = []
        s3 = -math.inf
        for n in nums[::-1]:
            if n < s3:
                return True
            while stack and stack[-1] < n:
                s3 = stack.pop()
            stack.append(n)
        return False