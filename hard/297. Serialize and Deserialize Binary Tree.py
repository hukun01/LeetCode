# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        '''
        1/2 Recursive: build the string list in preorder.
        '''
        def buildString(node, values):
            if node:
                values.append(str(node.val))
                buildString(node.left, values)
                buildString(node.right, values)
            else:
                values.append("#")

        values = []
        buildString(root, values)
        return ','.join(values)
        '''
        2/2 Iterative: build the string list in level order. 
        Use a nullCount to avoid adding '#' for the last level.
        '''
        if not root:
            return None
        queue = collections.deque([root])
        values = []
        nullCount = 0
        while queue:
            node = queue.popleft()
            if not node:
                # values.append("#")
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
        '''
        1/2 Recursive: the key is to pop the value list in every call.
        '''
        def buildTree(values):
            strVal = values.popleft()
            if strVal == "#":
                return None
            else:
                node = TreeNode(int(strVal))
                node.left = buildTree(values)
                node.right = buildTree(values)
                return node

        values = deque(data.split(','))
        return buildTree(values)
        """ 2/2 Iterative: Same as the string building process, build nodes in level order.
        """
        if not data:
            return None
        values = collections.deque(data.split(','))
        root = TreeNode(int(values.popleft()))
        nodeQueue = collections.deque([root])
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