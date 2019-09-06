class Solution:
    def numSquares(self, n: int) -> int:
        """ 
        BFS, also a DP. Note that the size of the input is actually log(n),
        assuming each step takes constant time, then the worst case we need O(N) steps,
        N is the value of the input number. And N's size is log(N), so O(N) = O(2^(log(N))) = O(2^n)
        """
        squares = [i * i for i in range(int(n ** 0.5) + 1)]
        sums = set(squares)
        result = 1
        while n not in sums:
            sums = {x + y for x in sums for y in squares}
            result += 1
        return result