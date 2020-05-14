# 402. Remove K Digits
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        Greedy.
        Note that to have the highest impact on the value, we want
        to start removing digits from the most significant positions, namely,
        from left to right.
        We need to decide what digits to keep and what to remove, when seeing
        two digits, we always want to keep the smaller one. Hence, keeping a
        monotically increasing stack of digits would help achieve this goal.
        A corner case: if k is still greater than 0 after the whole scan,
        meaning we still can remove another k digits, we will remove the last
        part because they have the highest digits.
        '''
        stack = []
        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        
        stack = stack[:-k] if k else stack
        return "".join(stack).lstrip('0') or "0"