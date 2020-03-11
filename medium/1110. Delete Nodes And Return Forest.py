# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        '''
        Iterate through the tree and delete node as we go, similar to below method.
        Everytime I delete a node, I can determine what the new trees are instantly.
        If a node with children is deleted, its children becomes 2 new trees. Also,
        we need to update the node's parent to point to None.
        '''
        result = set([root])
        toDeleteSet = set(to_delete)
        def preorder(node, parent):
            if not node:
                return
            if node.val in toDeleteSet:
                toDeleteSet.remove(node.val)
                if node in result:
                    result.remove(node)
                if parent:
                    if node == parent.left:
                        parent.left = None
                    else:
                        parent.right = None
                result.add(node.left)
                result.add(node.right)
            
            preorder(node.left, node)
            preorder(node.right, node)
        
        preorder(root, None)
        return [n for n in result if n is not None]
        '''
        # iterate the tree once to get the node:parent mapping,
        # everytime I delete a node, I can determine what the new trees are instantly.
        # if a node with children is deleted, its children becomes 2 new trees;
        # if a leaf is deleted, update the parent
        if root is None:
            return []
        valToNode = dict()
        nodeToParent = dict()
        def preorder(node, parent):
            if node is None:
                return
            valToNode[node.val] = node
            nodeToParent[node] = parent
            preorder(node.left, node)
            preorder(node.right, node)
        
        preorder(root, None)
        for toDel in to_delete:
            node = valToNode[toDel]
            if node.left is not None:
                nodeToParent[node.left] = None
            if node.right is not None:
                nodeToParent[node.right] = None
            
            parent = nodeToParent.pop(node, None)
            if parent is None:
                continue
                
            if parent.left and parent.left.val == toDel:
                parent.left = None
            else:
                parent.right = None
        
        return [node for node, parent in nodeToParent.items() if parent is None]
        '''