# 572. Subtree of Another Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        '''
        Transform trees into strings and do string match.
        Transform the two trees into string, and use built-in str.find() to
        check if t is a substring of s.
        To convert the tree into string, do any traversal, but remember to add
        null nodes as well to ensure the tree structure is consistent.
        Also, add an empty char to the begnning of the tree array, this is to
        ensure we don't mistakenly match "12,x,x" with "2,x,x", by changing it
        to ",12,x,x" and ",2,x,x".

        Time: O(|s| + |t|)
        Space: O(|s| + |t|)
        '''
        def preorder(node, arr):
            if not node:
                arr.append('#')
                return

            arr.append(str(node.val))
            preorder(node.left, arr)
            preorder(node.right, arr)

        arr1 = ['']
        preorder(s, arr1)

        arr2 = ['']
        preorder(t, arr2)

        tree1 = ','.join(arr1)
        tree2 = ','.join(arr2)

        return tree1.find(tree2) != -1