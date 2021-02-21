# 1766. Tree of Coprimes
class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        '''
        DFS with tricky constraints.
        The key constraint is 1 <= nums[i] <= 50. This tells that there will
        be many duplicate values in the tree.
        When doing DFS, we collect the ancestor nodes in the dictionary, whose
        key is the node value, value is a list of (node, depth) info.
        Then for every node, we can look into the ancestor mapping and see if
        there's any ancestor with coprime, and pick the one with the largest
        depth.
        Note that we need to backtrack the ancestor to prevent mixing the
        ancestors between different branches.

        Time: O(k n) where k is the value range of nums[i]
        Space: O(n) as we need to store the tree in a adjacency list.
        '''
        n = len(nums)
        tree = defaultdict(set)
        for a, b in edges:
            tree[a].add(b)
            tree[b].add(a)

        ans = [-1] * n
        visited = set()
        val2parents = defaultdict(list)

        def dfs(node, parent, depth):
            if node in visited:
                return
            visited.add(node)
            max_dep_parent = -1
            max_depth = -1
            for prev_parent_val, prev_parents in val2parents.items():
                if gcd(prev_parent_val, nums[node]) != 1:
                    continue
                if prev_parents:
                    prev_parent, prev_depth = prev_parents[-1]
                    if prev_depth > max_depth:
                        max_depth = prev_depth
                        max_dep_parent = prev_parent
            ans[node] = max_dep_parent

            val2parents[nums[node]].append((node, depth))
            for nex in tree[node]:
                if nex != parent:
                    dfs(nex, node, depth + 1)
            val2parents[nums[node]].pop()

        dfs(0, -1, 0)
        return ans