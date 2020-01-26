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
        distance = [0] * N
        childNodeCount = [1] * N
        tree = collections.defaultdict(list)
        for parent, child in edges:
            tree[parent].append(child)
            tree[child].append(parent)
        
        # Get the childNodeCount for each node, and distance from the node to
        # its subtree nodes.
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