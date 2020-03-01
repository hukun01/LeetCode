class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        '''
        Use a defaultdict(set) to store the val: {idx1, idx2} mapping.
        Remember to update the idx when removing a val.
        '''
        self.dict = collections.defaultdict(set)
        self.list = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.list.append(val)
        self.dict[val].add(len(self.list)-1)
        return len(self.dict[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if len(self.dict[val]) == 0:
            return False
        idx = self.dict[val].pop()
        if idx != len(self.list) - 1:
            lastVal = self.list[-1]
            self.list[idx] = lastVal
            self.dict[lastVal].remove(len(self.list) - 1)
            self.dict[lastVal].add(idx)
        self.list.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()