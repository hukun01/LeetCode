# 1643. Kth Smallest Instructions
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        '''
        Math.
        'H' is smaller than 'V', hence at index i of any solution,
        placing 'H' would make the result smaller than placing 'V'.
        Smaller than how many? Say (x) results would be smaller.
        x = nCr, where n is the remaining total steps, r is the
        remaining v steps.
        If k is less than or equal to x, we need to put 'H' at i,
        otherwise we put a 'V' there, and subtract x from k, meaning
        k will now be larger than (k-x) results.
        '''
        V, H = destination
        ans = []
        remaining_v = V
        for i in range(V + H):
            remaining_steps = V + H - (i + 1)
            x = math.comb(remaining_steps, remaining_v)
            if x >= k:
                ans.append('H')
            else:
                remaining_v -= 1
                k -= x
                ans.append('V')
        return ''.join(ans)