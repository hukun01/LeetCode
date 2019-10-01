class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Say the current sum of the array is sum, the length of nums is n, 
        # and the original minimum is minNum
        # Assuming after m moves we reach the state where every element is x,
        # then we have sum + (n-1) * m = n * x;
        # and x = minNum + m.
        # The second equation can be derived from the fact that every time
        # when we make the move, all elements are incremented except the max one,
        # and every other number could be the max one, except minNum, so minNum
        # will use exactly m moves to reach x.
        # Hence, after combining two equations, we have m = sum - n*minNum
        return sum(nums) - len(nums) * min(nums)