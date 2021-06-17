# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    '''
    1/2 Recursive - preorder traversal.

    Serialize: build the string list in preorder.

    Deserialize: the key is to popleft the value list in every call.
    '''
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = []
        def preorder(node):
            if not node:
                ans.append('#')
                return
            ans.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ','.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = deque(data.split(','))
        def preorder():
            if not data:
                return None
            val = data.popleft()
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = preorder()
            node.right = preorder()
            return node

        return preorder()

    '''
    2/2 Iterative - level order traversal.

    Serialize: Build the string list in level order. 
    Use a nullCount to avoid adding '#' for the last level.

    Deserialize: similar to the serialize process, build nodes in level order.
    '''
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None
        queue = collections.deque([root])
        values = []
        nullCount = 0
        while queue:
            node = queue.popleft()
            if not node:
                # Instead of `values.append("#")`, increment nullCount.
                nullCount += 1
                continue
            values.extend(["#" for _ in range(nullCount)])
            nullCount = 0
            values.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        return ','.join(values)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        values = deque(data.split(','))
        root = TreeNode(int(values.popleft()))
        nodeQueue = deque([root])
        while values:
            parent = nodeQueue.popleft()
            val = values.popleft()
            if val != "#":
                parent.left = TreeNode(int(val))
                nodeQueue.append(parent.left)
            if values:
                val = values.popleft()
                if val != "#":
                    parent.right = TreeNode(int(val))
                    nodeQueue.append(parent.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))