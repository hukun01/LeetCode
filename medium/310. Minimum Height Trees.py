# 310. Minimum Height Trees
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        Topological sort.
        The roots with min heights must be the ones in the middle.
        Start from the leaves (nodes with one neighbor), remove them
        from the tree, and remove them from their neighbors, so some
        of the neighbors become leaves. Keep doing this until the total
        number of nodes become 1 or 2, then the current leaves would be
        the roots with min heights. It's one or two because either can
        form a tree where we can find min height trees, it can't go up to
        3 otherwise the graph must have a cycle.

        One edge case is that if there is 0 edges and just 1 node, [0]
        is the answer.
        '''
        tree = defaultdict(set)
        for a, b in edges:
            tree[a].add(b)
            tree[b].add(a)
        leaves = [node for node, neighbors in tree.items() if len(neighbors) == 1]
        while len(tree) > 2:
            new_leaves = []
            for l in leaves:
                for neighbor in tree.pop(l):
                    tree[neighbor].remove(l)
                    if len(tree[neighbor]) == 1:
                        new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves or [0]