# 1300. Sum of Mutated Array Closest to Target
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        '''
        1/2 Binary search
        Try values between 0 and max(arr), find the value that's closest to target.
        To break tie, double check [l-1, l, l+1] to find the min val.
        '''
        l, h = 0, max(arr)

        def mySum(val):
            return sum(min(a, val) for a in arr)

        while l < h:
            m = (l + h) // 2
            if mySum(m) < target:
                l = m + 1
            else:
                h = m
        return min(l - 1, l, l + 1, key=lambda x: abs(mySum(x) - target))
        '''
        2/2 Sort reversely
        Only bigger numbers matter, so we sort the array reversely, and
        check each min number from the tail, if it's not good, we pop it out,
        and remove it from the target, considering it no longer impacting the result.
        A min number is not good if min * len(arr) < target.
        We stop when min * len(arr) >= target, at this time we can split the
        target evenly based on the count of remaining numbers.
        Since we need to return the min val, when there's a tie, 
        '''
        arr.sort(reverse = 1)
        maxA = max(arr)
        while arr and arr[-1] * len(arr) < target:
            target -= arr.pop()
            
        def mySum(val):
            return sum(min(a, val) for a in arr)

        if arr:
            c = target // len(arr)
            return min(c - 1, c, c + 1, key=lambda x: abs(mySum(x) - target))
        else:
            return maxA