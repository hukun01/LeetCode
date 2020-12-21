# 880. Decoded String at Index
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        '''
        Math.
        Direction: A fully decoded string will be too big and wasteful, we aim
        to find a way to locate the char without decoding the string.

        Track the current size of the decoded string, without decoding it.
        When cur_size >= K, break out the loop. From the index where we
        stopped, walk backward. In each round, K %= cur_size, as we 'zoom in',
        Then reduce the cur_size similar to how we increased it - if char is
        digit, divide cur_size by it, otherwise minus one from cur_size.
        Whenever K is 0 and char is letter, return char.

        Time: O(n)
        Space: O(1)
        '''
        cur_size = 0
        for i in range(len(S)):
            if S[i].isdigit():
                cur_size *= int(S[i])
            else:
                cur_size += 1
            if cur_size >= K:
                break
        for x in range(i, -1, -1):
            K %= cur_size
            c = S[x]
            if c.isdigit():
                cur_size //= int(c)
            else:
                cur_size -= 1
                if K == 0:
                    return c