# 396. Rotate Function
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        '''
        F(k)   = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]
        F(k-1) = 0 * Bk-1[0] + 1 * Bk-1[1] + ... + (n-1) * Bk-1[n-1]
               = 0 * Bk[1] + 1 * Bk[2] + ... + (n-2) * Bk[n-1] + (n-1) * Bk[0]
        Then
        F(k) - F(k-1) = Bk[1] + Bk[2] + ... + Bk[n-1] + (1-n)Bk[0]
                      = (Bk[0] + ... + Bk[n-1]) - nBk[0]
                      = sum(A) - nBk[0]
        And F(k) = F(k-1) + sum(A) - nBk[0]
        
        Start k from 1, 
        F(1) = F(0) + sum - nB1[0], k = 1, B1[0] = A[-1]
        F(2) = F(1) + sum - nB2[0], k = 2, B1[0] = A[-2]...
        
        Note that we only use elements in A once from backward.
        '''
        ans = curr = sum(i * n for i, n in enumerate(A))
        total = sum(A)
        n = len(A)
        while A:
            curr += total - A.pop() * n
            ans = max(ans, curr)
            
        return ans