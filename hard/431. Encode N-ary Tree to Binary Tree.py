"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
class Codec:
    '''
    Convert the current Node to a TreeNode;
    Convert the first Node child into the TreeNode's right child (rc), 
    and convert the rest of the Node children (rc's siblings) into rc's left child.
    
    Essentially, let rc manage its unbounded siblings with its left child chain.
    '''
    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        
        :type root: Node
        :rtype: TreeNode
        """
        if not root:
            return None
        current = node = TreeNode(root.val)
        if root.children:
            current.right = self.encode(root.children[0])
            current = current.right
            for c in root.children[1:]:
                current.left = self.encode(c)
                current = current.left
        return node

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        
        :type data: TreeNode
        :rtype: Node
        """
        if not data:
            return None
        node = Node(data.val, [])
        child = data.right
        while child:
            node.children.append(self.decode(child))
            child = child.left
        return node
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))