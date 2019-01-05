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
        self.nodes = []
        if not root:
            return
        self.nodes.append(root)
        for node in self.nodes:
            if node.left:
                self.nodes.append(node.left)
            if node.right:
                self.nodes.append(node.right)
                
    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        newNode = TreeNode(v)
        self.nodes.append(newNode)
        idx = len(self.nodes) - 1
        parentIdx = (idx - 1) // 2
        parentNode = self.nodes[parentIdx]
        if idx % 2 == 1:
            parentNode.left = newNode
        else:
            parentNode.right = newNode
        return parentNode.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.nodes[0]


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()