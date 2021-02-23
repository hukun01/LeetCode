# 1110. Delete Nodes And Return Forest
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        '''
        DFS.
        Key is to start from a set 'ans' with root node in it.
        Preorder iterate through the tree and delete node as we go.
        We keep going down, if a node is in delete set, discard it from 'ans'.
        Everytime a node is deleted, we know the potential new trees - if
        it has children, its children becomes 2 new trees. Also, we need
        to update the node's parent to point to None.
        '''
        ans = set([root])
        to_delete = set(to_delete)
        def preorder(node, parent):
            if not node:
                return
            if node.val in to_delete:
                ans.discard(node)
                if parent:
                    if node == parent.left:
                        parent.left = None
                    else:
                        parent.right = None
                ans.add(node.left)
                ans.add(node.right)
            
            preorder(node.left, node)
            preorder(node.right, node)

        preorder(root, None)
        ans.discard(None)
        return list(ans)