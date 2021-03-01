# Maximum Frequency Stack
class FreqStack:
    '''
    '''

    def __init__(self):
        self.freq = Counter()
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, x: int) -> None:
        self.freq[x] += 1
        f = self.freq[x]
        self.group[f].append(x)
        if f > self.max_freq:
            self.max_freq = f

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