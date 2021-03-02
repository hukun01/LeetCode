# 895. Maximum Frequency Stack
class FreqStack:
    '''
    Stack of stacks.
    We need to track the values that have max_freq, also in the order that they
    were pushed. Use a counter to track the frequencies for each value. Use a
    mapping {freq: values} to track the frequency and the values that are
    pushed at that frequency level. Note that all elements in each 'values'
    would be unique, because each value can have one unique frequency, before
    we increment it.
    During this process, record the max_freq. When pop(), start from max_freq.

    Time: O(1) for push and pop.
    Space: O(n) where n is total number of pushed values.
    '''

    def __init__(self):
        self.freq = Counter()
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, x: int) -> None:
        self.freq[x] += 1
        self.group[self.freq[x]].append(x)
        self.max_freq = max(self.max_freq, self.freq[x])

    def pop(self) -> int:
        x = self.group[self.max_freq].pop()
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        self.freq[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()