# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        '''
        1/3 Recursive approach.
        Knowing below:
        preorder = [root, left_sub_tree, right_sub_tree]
        inorder = [left_sub_tree, root, right_sub_tree]

        We can use the first element from preorder as the root, and locate it
        in inorder, so to find out the left and right sub tree sizes. Then we
        recursively process the left part to get the left subtree, and similar
        to the right part.

        Time: O(n)
        Space: O(n)
        '''
        val_to_idx = {v:i for i, v in enumerate(inorder)}
        def build(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r:
                return None
            root = TreeNode(preorder[pre_l])
            root_idx_inorder = val_to_idx[root.val]
            left_sub_tree_size = root_idx_inorder - in_l
            root.left = build(pre_l+1, pre_l + 1 + left_sub_tree_size - 1, in_l, in_l + left_sub_tree_size - 1)
            root.right = build(pre_l + 1 + left_sub_tree_size, pre_r, root_idx_inorder + 1, in_r)
            return root
        
        n = len(preorder)
        return build(0, n - 1, 0, n - 1)
        
        '''
        2/3 Another recursive without the map!
        Each recursive call gets told where to stop, and it tells its subcalls
        where to stop. It gives its own root value as stopper to its left
        subcall, and gives its parent`s stopper as stopper to its right
        subcall. Essentially, this is the same as above - using preorder to
        locate the root value, and using inorder to locate the left and right
        subtrees.

        Note that the pop(0) here expensively O(n) time, but it is to better
        illustrate the idea, we can reverse both arrays so we can do pop() that
        takes O(1) time.

        Time: O(n)
        Space: O(n)
        '''
        def build(stop):
            if inorder and inorder[0] != stop:
                root = TreeNode(preorder.pop(0))
                root.left = build(root.val)
                inorder.pop(0)
                root.right = build(stop)
                return root
        return build(None)
        '''
        3/3 Iterative approach
        '''
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