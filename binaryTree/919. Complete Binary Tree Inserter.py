# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter:
    
    def __init__(self, root):
        """
        :type root: TreeNode

        Notice that this class is used to help insert nodes to a COMPLETE binary tree,
        it shouldn't re-create the entities, but just store their references.
        Since the tree is complete, we can find its parent in O(1) time, so to make 
        insertion easy.
        """
        self._tree = [root]
        for node in self._tree:
            if node.left:
                self._tree.append(node.left)
            if node.right:
                self._tree.append(node.right)
                
    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        self._tree.append(TreeNode(v))
        N = len(self._tree)
        if N % 2 == 0:
            self._tree[(N - 2) // 2].left = self._tree[-1]
        else:
            self._tree[(N - 2) // 2].right = self._tree[-1]
        return self._tree[(N - 2) // 2].val
            
    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self._tree[0]


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()