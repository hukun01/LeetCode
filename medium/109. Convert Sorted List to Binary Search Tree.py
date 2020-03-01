# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
        """
        """ 1/2 Convert the list to an array, and build BST from there
        O(N) time, O(N) space for the array (not counting TreeNode creation space)
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        def buildBST(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(arr[mid])
            root.left = buildBST(left, mid - 1)
            root.right= buildBST(mid + 1, right)
            return root
        return buildBST(0, len(arr) - 1)
        """
        """ 2/2 Build tree using inorder (inorder traversal is highly related to BST)
        O(N) time, O(logN) space (not counting TreeNode creation space)
        """
        def inorder(left, right): # left and right are used as boundary to tell when to end
            if left > right: # no equal here!
                return None
            mid = left + (right - left) // 2
            
            # build the left sub tree, note that we don't include mid here
            leftNode = inorder(left, mid - 1)

            # build the root, and link to the left sub tree
            nonlocal node
            root = TreeNode(node.val)
            root.left = leftNode

            # every time when we create a new TreeNode which uses node.val, we move the node to the next.
            # whenever we are done building the left sub tree, we should have created (mid - left - 1) nodes,
            # then the head will point to the middle node 
            node = node.next # critical to move to the next!

            # build the right sub tree
            root.right = inorder(mid + 1, right)
            return root
        nodeCount = 0
        node = head
        while head:
            nodeCount += 1
            head = head.next
        return inorder(1, nodeCount) # Use 1 as the left bound as the node count.