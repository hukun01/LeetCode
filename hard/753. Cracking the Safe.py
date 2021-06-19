# 753. Cracking the Safe
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        '''
        Euler path.

        We need to traverse each node at least once in the graph, where a node
        is a possible password permutation.
        To make the traversal path minimum, we only visit each node once, so
        this transforms the problem into finding the Euler path in the graph.

        Time: O(n V) where V is the number of nodes, which is k^n
        Space: O(V)
        '''
        ans = []
        seen = set()
        def dfs(node):
            for i in range(k):
                nex = node + str(i)
                if nex not in seen:
                    seen.add(nex)
                    dfs(nex[1:])
                    ans.append(str(i))

        dfs("0" * (n - 1))
        return "".join(ans) + "0" * (n - 1)