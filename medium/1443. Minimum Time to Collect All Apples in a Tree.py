# 1443. Minimum Time to Collect All Apples in a Tree
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        '''
        Build the tree and do DFS.
        '''
        tree = [[] for _ in range(n)]
        for f, t in edges:
            tree[f].append(t)
            tree[t].append(f)

        # Return the number of steps to reach all apples under 'node' and come back
        # to the 'node'. Return 0 if no apples found.
        def dfs(parent, node):
            steps = 0
            for c in tree[node]:
                if c != parent:
                    steps += dfs(node, c)

            # If the node itself has an apple, or its children have apples, and this
            # node is not the start (0), we need to go to it and come back, so adding
            # 2 to the steps.
            if (hasApple[node] or steps > 0) and node != 0:
                steps += 2
            return steps
        return dfs(-1, 0)