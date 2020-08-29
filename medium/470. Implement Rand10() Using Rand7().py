# 470. Implement Rand10() Using Rand7()
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        '''
        Math.
        rand7() -> rand49() -> rand40() -> rand10().
        Generalization: from randX() to randY().
        Say k is in [1, Y], P(randM() = k) = 1/M, where M >= Y, we need
        P(result = k) =
            P(randM() = k in the 1st iteration) +
            P(randM() > Y in the 1st iteration) * P(randM() = k in the 2nd iteration) +
            P(randM() > Y in the 1st iteration) * P(randM() > Y in the 2nd iteration) * P(randM() = k in the 3rd iteration) +
            ...
        = (1/M) * (1 + (M-Y)/M + ((M-Y)/M) ^ 2 + ...)
        = (1/M) * (M/Y)
        = (1/Y)
        Hence, we can use randX(), to do 
        N^b * (randX() - 1) + N^(b-1) * (randX() - 1) + ... + (randX() - 1)
        to generate (randM() - 1). We then keep computing result which is
        (randM() - 1), until it is less than (not equal to) Y*n, where Y*n <= M.
        Then final result is (randM() - 1) % Y + 1.
        '''
        result = 40
        while result >= 40:
            result = 7 * (rand7() - 1) + (rand7() - 1)
        return result % 10 + 1