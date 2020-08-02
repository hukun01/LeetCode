# 984. String Without AAA or BBB
class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        '''
        Greedy.
        '''
        ans = [''] * (A + B)
        for i in range(len(ans)):
            if i >= 2 and ans[i-1] == ans[i-2]:
                use_a = ans[i-1] == 'b'
            else:
                use_a = A >= B
            if use_a:
                A -= 1
                ans[i] = 'a'
            else:
                B -= 1
                ans[i] = 'b'
        return ''.join(ans)