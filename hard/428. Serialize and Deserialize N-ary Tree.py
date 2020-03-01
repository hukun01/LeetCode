"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:
    '''
    dfs encode the tree, at each level, add the count of the children
    at that level, so that we know when to stop a level when decoding.
    '''
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        vals = []
        def encode(node):
            if not node:
                return
            vals.append(str(node.val))
            vals.append(str(len(node.children)))
            for c in node.children:
                encode(c)
        encode(root)
        return ' '.join(vals)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        vals = collections.deque(data.split(' '))
        def decode():
            val = int(vals.popleft())
            size = int(vals.popleft())
            root = Node(val, [])
            for c in range(size):
                root.children.append(decode())
            return root
        
        return decode()
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))