# 1483. Kth Ancestor of a Tree Node
class TreeAncestor:
    '''
    DP.
    Let dp[i][j] be the (2^j)th parent of the i-th node.
    Then we have dp[i][j] = dp[dp[i][j - 1]][j - 1], the number of steps
    from i to kth parent is cut in half comparing to linear approach.
    '''

    def __init__(self, n: int, parent: List[int]):
        m = 1 + int(log2(n))
        self.dp = [[-1] * m for _ in range(n)] #ith node's 2^j parent
        for j in range(m):
            for i in range(n):
                if j == 0:
                    self.dp[i][0] = parent[i] #2^0 parent
                elif (half_parent := self.dp[i][j-1]) != -1: 
                    self.dp[i][j] = self.dp[half_parent][j-1]
    
    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1: 
            i = int(log2(k))
            node = self.dp[node][i]
            k -= (1 << i)
        return node 


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)