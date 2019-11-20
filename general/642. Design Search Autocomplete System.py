class Node:
    def __init__(self, c):
        self.c = c
        self.times = 0
        self.children = {}

class AutocompleteSystem:
    '''
    Use trie tree to record all sentences and times.
    Use DFS to find all applicable sentences; use heap to find the top sentences.
    '''
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Node("")
        self.setupTrie(sentences, times)
        self.reset()
            
    def reset(self):
        self.currNode = self.root
        self.search = []
        
    def setupTrie(self, sentences: List[str], times: List[int]):
        for sentence, time in zip(sentences, times):
            parent = self.root
            for i, c in enumerate(sentence):
                if c in parent.children:
                    child = parent.children[c]
                else:
                    child = Node(c)
                    parent.children[c] = child
                if i == len(sentence) - 1:
                    child.times = time
                parent = child
    
    def find(self):
        ans = []
        def dfs(node, currSentence):
            if node.times > 0:
                heapq.heappush(ans, (-node.times, "".join(currSentence)))
            for child in node.children.values():
                currSentence.append(child.c)
                dfs(child, currSentence)
                currSentence.pop()
        dfs(self.currNode, self.search)
        result = []
        while ans and len(result) < 3:
            pair = heapq.heappop(ans)
            result.append(pair[1])
        return result

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.currNode.times += 1
            self.reset()
            return []
        self.search.append(c)
        if c in self.currNode.children:
            self.currNode = self.currNode.children[c]
        else:
            child = Node(c)
            self.currNode.children[c] = child
            self.currNode = child
        return self.find()

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)