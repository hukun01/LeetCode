# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        """ 1/3 Recursive approach:
        def buildTree(preorder, pLeft, pRight, inorder, iLeft, iRight, inorderDict):
            if pLeft > pRight:
                return None
            root = TreeNode(preorder[pLeft])
            rootIndex = inorderDict[root.val]
            leftTreeSize = rootIndex - iLeft
            root.left = buildTree(preorder, pLeft + 1, pLeft + leftTreeSize, \
                                 inorder, iLeft, rootIndex - 1, inorderDict)
            root.right = buildTree(preorder, pLeft + leftTreeSize + 1, pRight, \
                                  inorder, rootIndex + 1, iRight, inorderDict)
            return root
        
        inorderDict = { k : v for v, k in enumerate(inorder) }
        return buildTree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, inorderDict)
        """
        """ 2/3 Another recursive without the map!
        Each recursive call gets told where to stop, and it tells its subcalls where to stop. 
        It gives its own root value as stopper to its left subcall, 
        and gives its parent`s stopper as stopper to its right subcall.
        Essentially, this is the same as above - using preorder to locate the root value, and 
        using inorder to locate the left and right subtrees.

        def build(stop):
            if inorder and inorder[0] != stop:
                root = TreeNode(preorder.pop(0))
                root.left = build(root.val)
                inorder.pop(0)
                root.right = build(stop)
                return root
        return build(None)
        """
        """ 3/3 Iterative approach:
        """
        if not preorder:
            return None
        inorderMap = { k : v for v, k in enumerate(inorder) }
        root = TreeNode(preorder[0])
        stack = [root]
        for val in preorder[1:]:
            node = TreeNode(val)
            if inorderMap[val] < inorderMap[stack[-1].val]:
                # The new node is at the left of the last node, in inorder,
                # so the new one must be the direct left child of the last node,
                # that's the way *preorder* works.
                stack[-1].left = node
            else:
                # The new node is at the right of the last node, in inorder,
                # so it must be the right child of either:
                # 1. the last node 
                # 2. or one of the last nodes' ancestors
                # Pop the stack until we either run out of ancestors or 
                # the node at the top of the stack is at the right of the new node in inorder,
                # then the current node we have is the last node at the left of new node in inorder,
                # meaning that the new node is the direct right child of the current node, based on inorder.
                while stack and inorderMap[val] > inorderMap[stack[-1].val]:
                    parent = stack.pop()
                parent.right = node
            stack.append(node)
        return root