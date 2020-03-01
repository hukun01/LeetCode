class RandomizedSet:
    '''
    Use a list and random.choice(list) to achieve randomized get().
    Use a dictionary to make insert O(1) in average;
    But now we also need to update the list, how to make remove O(1)?
    Let the dictionary store the index of each number in the list. When removing an
    element from the dict, grab its index, and swap the values in the list with the tail,
    when the index itself is not at tail. Update dict with the new index if there is any.
    Then pop the list.
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.locations = dict()
        self.li = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.locations:
            return False
        self.li.append(val)
        self.locations[val] = len(self.li) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.locations:
            return False
        idx = self.locations[val]
        self.locations.pop(val)
        if idx < len(self.li) - 1:
            lastVal = self.li[-1]
            self.li[idx] = lastVal
            self.locations[lastVal] = idx
        self.li.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.li)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()