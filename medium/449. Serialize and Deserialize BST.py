# 449. Serialize and Deserialize BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    '''
    Preorder traversal.
    Serializing the BST using its insertion order.
    When deserializing, as we know this is a BST, we can iterate through
    the values in inseration order, and use lower_bound and upper_bound to
    determine whether the next value should be inserted under the current
    subtree, or it should go to another branch.
    '''

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        ans = []
        def preorder(node):
            if not node:
                return
            ans.append(node)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ','.join(str(n.val) for n in ans)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return
        vals = deque(data.split(','))
        def dfs(lb, ub):
            if not vals:
                return
            val = int(vals[0])
            if val < lb or val > ub:
                return
            vals.popleft()
            node = TreeNode(val)
            node.left = dfs(lb, val)
            node.right = dfs(val, ub)
            return node
        return dfs(-math.inf, math.inf)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans