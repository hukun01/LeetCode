# 310. Minimum Height Trees
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        Topological sorting.
        The roots with min heights must be the ones in the middle.
        Start from the leaves (nodes with one neighbor), remove them
        from the tree, and remove them from their neighbors, so some
        of the neighbors become leaves. Keep doing this until the total
        number of nodes become 1 or 2, then the current leaves would be
        the roots with min heights.
        One edge case is that if there is no edges and just 1 node, [0]
        is the answer.
        '''
        tree = [set() for _ in range(n)]
        for a, b in edges:
            tree[a].add(b)
            tree[b].add(a)
        leaves = [node for node, neighbors in enumerate(tree) if len(neighbors) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for l in leaves:
                single_neighbor = tree[l].pop()
                tree[single_neighbor].remove(l)
                if len(tree[single_neighbor]) == 1:
                    new_leaves.append(single_neighbor)
            leaves = new_leaves
        return leaves if leaves else [0]