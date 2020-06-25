# 742. Closest Leaf in a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        '''
        1/2 DFS + BFS.
        DFS find the k node and the parent-child path, then BFS from the k_node
        to find the closest leaf node.
        Time is O(n) because when k is the root in a full tree, BFS will
        traverse most nodes except the bottom level.
        '''
        def dfs(node, path):
            if not node:
                return
            path.append(node)
            if found := dfs(node.left, path) or dfs(node.right, path):
                return found
            if node.val == k:
                return node
            path.pop()
        
        path_to_k = []
        k_node = dfs(root, path_to_k)

        child_to_parent = { child: parent for parent, child in zip(path_to_k, path_to_k[1:]) }
        visited = set()
        queue = [k_node]
        for node in queue:
            if not node or node.val in visited:
                continue
            visited.add(node.val)
            if node.left == node.right == None:
                return node.val
            next_nodes = [child_to_parent.get(node), node.left, node.right]
            queue += next_nodes
        raise KeyError("No solution")
        '''
        2/2 DFS + DFS.
        Similarly, use DFS to find the k node and parent-child path, and
        construct the ancestor-distance_to_k mapping.
        DFS find the closest leaf node from root, if the node is in the
        distance mapping, use it, otherwise use the parent_distance + 1.
        '''
        def find_k_ancestor(node):
            if not node:
                return None
            if node.val == k:
                return [node.val]
            ancestors = find_k_ancestor(node.left) or find_k_ancestor(node.right)
            if ancestors:
                ancestors.append(node.val)
            return ancestors
        
        dist_to_k = {ancestor: dist for dist, ancestor in enumerate(find_k_ancestor(root))}
        self.res = (math.inf, None)
        
        def find_dist_to_k(node, parent_dist):
            if not node or parent_dist > self.res[0]:
                return
            dist = dist_to_k.get(node.val, parent_dist + 1)
            if node.left == node.right == None:
                self.res = min(self.res, (dist, node.val))
                return
            find_dist_to_k(node.left, dist)
            find_dist_to_k(node.right, dist)
        
        find_dist_to_k(root, 0)
        return self.res[1]