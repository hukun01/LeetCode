'''
1166. Design File System

1/2 Build the file system as a tree.

Use a path node that's like a tree node. 
'''

class Path:
    
    def __init__(self, value):
        self.val = value
        self.subfolders = {}

class FileSystem:

    def __init__(self):
        self.root = Path(0)
        self.root.subfolders[""] = Path(0)

    def createPath(self, path: str, value: int) -> bool:
        parts = path.split('/')
        root = self.root
        for i, part in enumerate(parts):
            if part in root.subfolders:
                root = root.subfolders[part]
                continue
            if i == len(parts) - 1:
                root.subfolders[part] = Path(value)
                return True
            else:
                return False
                
        return False

    def get(self, path: str) -> int:
        root = self.root
        parts = path.split('/')
        for part in parts:
            if part not in root.subfolders:
                return -1
            root = root.subfolders[part]
        return root.val

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

'''
2/2 Use a dict to store all path to value mappings. For all create requests,
use path.rfind('/') to find the rightmost index of '/', and get the parent
path, only when parent path exists, we create the path.
We need to add "":-1 to the initial paths mappings.

class FileSystem:

    def __init__(self):
        self.pathToValue = { "": -1 }

    def createPath(self, path: str, value: int) -> bool:
        parent = path[:path.rfind('/')]
        if parent in self.pathToValue and path not in self.pathToValue:
            self.pathToValue[path] = value
            return True
        return False

    def get(self, path: str) -> int:
        return self.pathToValue.get(path, -1)
'''