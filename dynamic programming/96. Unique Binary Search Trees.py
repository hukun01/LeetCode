class Solution:
    def numTrees(self, n: int) -> int:
        '''
        G(n): the number of unique BST for a sequence of length n.
        F(i, n), 1 <= i <= n: the number of unique BST, where the number i 
        is the root of BST, and the sequence ranges from 1 to n.

        G(n) = F(1, n) + F(2, n) + ... + F(n, n)
        F(i, n) = G(i-1) * G(n-i), 1 <= i <= n 
        Combining the above, we have
        G(n) = G(0) * G(n-1) + G(1) * G(n-2) + ... + G(n-1) * G(0)

        And we have G(0)=1, G(1)=1

        In terms of calculation, we need to start with the lower number, 
        since the value of G(n) depends on the values of G(0) … G(n-1).
        '''
        nums = [0 for _ in range(n + 1)]
        nums[0] = nums[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                nums[i] += nums[j - 1] * nums[i - j]
        return nums[n]