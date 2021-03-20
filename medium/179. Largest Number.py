# 179. Largest Number
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        '''
        Sort.
        The key here is how we compare "82" and "827" - if we use "827"
        first because we prefer longer numbers, we get "827 82", while "82 827"
        is bigger. If we use "82" first because we prefer shorter numbers,
        we get "82 827", but if we also have "829", we get "82 829 827", while
        "829 82 827" is the biggest.
        The trick is to compare "a+b" and "b+a", instead of just "a" and "b".

        Time: O(n log(n)) where n is len(nums)
        Space: O(n)
        '''
        def compare(a, b):
            if (c1 := a + b) < (c2 := b + a):
                return 1
            elif c1 > c2:
                return -1
            return 0

        ans = sorted((str(a) for a in nums), key=functools.cmp_to_key(compare))

        return ''.join(ans).lstrip('0') or '0'