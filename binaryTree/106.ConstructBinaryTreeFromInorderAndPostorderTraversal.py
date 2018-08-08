# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        The use of postorder is to find the root; 
        the use of inorder is to find the left subtree and the right subtree.
        Also use a inorderDict to have fast access to root index.

        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        """ Recursive approach:
        def buildTree(inorder, iLeft, iRight, postorder, pLeft, pRight, inorderDict):
            if iLeft > iRight:
                return None
            root = TreeNode(postorder[pRight])
            rootIndex = inorderDict[root.val]
            leftTreeSize = rootIndex - iLeft
            root.left = buildTree(inorder, iLeft, rootIndex - 1, \
                                  postorder, pLeft, pLeft + leftTreeSize - 1, inorderDict)
            root.right = buildTree(inorder, rootIndex + 1, iRight, \
                                  postorder, pLeft + leftTreeSize, pRight - 1, inorderDict)
            return root

        inorderDict = { k : v for v, k in enumerate(inorder) }
        return buildTree(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1, inorderDict)
        """
        """ Iterative approach:
        """
        if not postorder:
            return None
        inorderMap = { k : v for v, k in enumerate(inorder) }
        postorder = postorder[::-1] # become [root, rightSubTree, leftSubTree]
        root = TreeNode(postorder[0])
        stack = [root]
        for val in postorder[1:]:
            node = TreeNode(val)
            if inorderMap[val] < inorderMap[stack[-1].val]:
                # The new node is at the left of the last node, in inorder,
                # so it must be the left child of either:
                # 1. the last node 
                # 2. or one of the last nodes' ancestors
                # Pop the stack until we either run out of ancestors or 
                # the node at the top of the stack is at the left of the new node
                while stack and inorderMap[val] < inorderMap[stack[-1].val]:
                    parent = stack.pop()
                parent.left = node
            else:
                # The new node is at the right of the last node, in inorder,
                # so the new one must be the direct RIGHT child of the last node,
                # that's the way *reversed postorder* works.
                stack[-1].right = node
            stack.append(node)
        return root