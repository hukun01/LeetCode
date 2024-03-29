# 402. Remove K Digits
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        Greedy with Conditional Mono Stack.
        Note that to have the highest impact on the value, we want
        to start removing digits from the most significant positions, namely,
        from left to right, we KEEP the smallest digits.
        When seeing two digits, we always want to keep the smaller one. Hence,
        keeping a monotically increasing stack of digits would help achieve
        this goal. If the current number 'a' is less than the stack top, and
        there's enough remaining digits to fill the stack up to k, we can keep
        poping the stack and replace the top with 'a'.
        This is a conditional mono stack because we only pop things out when
        there's enough remaining elements, otherwise we only append.

        A corner case: need to lstrip the leading 0s and return 0 when seeing
        output like '0000'.

        Time: O(n) where n is the length of the nums array.
        Space: O(k)
        Overall, in any problem that boils down to comparing two nearby
        elements, mono stack is a good thing to try.
        '''
        stack = []
        for a in num:
            while stack and k and stack[-1] > a:
                stack.pop()
                k -= 1
            stack.append(a)

        if k > 0:
            stack = stack[:-k]
        return ''.join(stack).lstrip('0') or '0'
