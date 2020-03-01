# 834. Sum of Distances in Tree
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        '''
        In linear time we can find sum of distances from root to all other nodes.

        When we move from root to a connected node X, one part of the nodes get
        closer to X, the rest gets further. If we know how many nodes on both
        sides for each node X, we know the distances between X and all other nodes.
        
        Note that this is an undirected tree, so the child node also needs to map
        back to its single parent.
        '''

        tree = collections.defaultdict(list)
        # At this point, we don't really know who's the parent/child because it's undirected.
        for n1, n2 in edges:
            tree[n1].append(n2)
            tree[n2].append(n1)

        distance = [0] * N
        childNodeCount = [1] * N
        
        # Get the childNodeCount for each node,
        # and distance from the node to its subtree nodes.
        # Note that after this dfs, the distance is only from node to all its subtree nodes,
        # but does not include distances to its sibling tree nodes and parents.
        def dfs(node, parent):
            for i in tree[node]:
                if i != parent:
                    dfs(i, node)
                    childNodeCount[node] += childNodeCount[i]
                    distance[node] += distance[i] + childNodeCount[i]
        
        def dfs2(node, parent):
            for i in tree[node]:
                if i != parent:
                    # childNodeCount[i] are closer to current node, (N - childNodeCount[i]) are further.
                    distance[i] = distance[node] - childNodeCount[i] + N - childNodeCount[i]
                    dfs2(i, node)
        
        dfs(0, -1)
        dfs2(0, -1)
        return distance