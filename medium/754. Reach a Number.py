# 754. Reach a Number
class Solution:
    def reachNumber(self, target: int) -> int:
        '''
        Math.
        First, notice that negative and positive target is the same, so just
        deal with abs(target).
        Let S = 1 + 2 + ... + k, and it's the smallest number >= target, the
        goal is to find a good k, such that we can set some of the signs to be
        positive and some negative, to reach target.
        As S = k * (1 + k) / 2 ~= k**2, we can start the k from sqrt(target),
        and try the next one or two k's until S >= target.

        We know that given a number x, if switch direction from right to left,
        the difference on S is 2*x.
        Let delta = S - target, we need to flip some numbers whose sum is
        T = delta // 2. Hence, if delta is even, we can always find subset of
        [1, k] that sums to T. If delta is odd, we need to try adding the next
        k to S, aka, S += k + 1, and now delta += k + 1, we keep doing this
        until delta becomes even. Obviously we only need to try adding S with
        up to (k + 2), to make delta even.

        Time: O(1)
        Space: O(1)
        '''
        target = abs(target)
        k = int((2*target)**0.5)
        while (S := k * (k+1) / 2) < target:
            k += 1

        while (S - target) % 2 == 1:
            k += 1
            S += k
        return k