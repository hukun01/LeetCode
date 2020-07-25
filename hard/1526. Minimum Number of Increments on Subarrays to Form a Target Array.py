# 1526. Minimum Number of Increments on Subarrays to Form a Target Array
class Solution:
    def minNumberOperations(self, T: List[int]) -> int:
        '''
        Whenever the current element a is bigger than the previous element,
        we need at lease (a - pre) operations to make up this difference.

        Another good explanation is to imagine that target arry as a list
        of walls, to build which we need to lay continous row of bricks.
        And we want to know the number of brick rows, which is the length
        of left edges of the walls, as shown below by '!'.

                +---+
                ! x |
                +---+---+
                ! x | x |
        +---+   +---+---+
        ! x |   ! x | x |
        +---+   +---+---+---+
        ! x |   ! x | x | x |
        +---+---+---+---+---+
        ! x | x | x | x | x |
        +---+---+---+---+---+
        '''
        return sum(max(T[i] - T[i-1], 0) for i in range(1, len(T))) + T[0]