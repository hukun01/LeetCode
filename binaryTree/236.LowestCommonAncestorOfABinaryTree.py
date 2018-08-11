# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        """ 1/2 Recursive: return the node if any of p or q is found, return None otherwise.
        Based on this, if we found non-Null results from both sides, 
        then the result is the current root. Otherwise would be the non-Null result.
        
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left:
            return left
        else:
            return right
        """
        """ 2/2 Iterative: We need to find the node chains that contain p and q, respectively, 
        so we have a way to track back to their ancestors. After we find both chains, 
        the first common node in two chains is the lowest common ancestor.
        """
        stack = [root]
        parentMapping = { root: None }
        while p not in parentMapping or q not in parentMapping:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parentMapping[node.left] = node
            if node.right:
                stack.append(node.right)
                parentMapping[node.right] = node
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parentMapping[p]
        while q not in ancestors:
            q = parentMapping[q]
        return q