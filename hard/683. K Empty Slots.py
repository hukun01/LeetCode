# 683. K Empty Slots
class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        '''
        Sliding window.

        Convert the input bulbs to bulb_to_day mapping, now we need to find
        all intervals [i, j] in which the min day is greater than the i-1 and
        j+1. This means that all bulbs within [i, j] would be turned on later
        than i-1 and j+1 bulb, so that after both bulbs are on, we get a valid
        interval if the size of [i, j] is exactly K.
        To find the min day within a K sliding window, we can use a min queue.
        '''
        n = len(bulbs)
        bulb_to_day = [0] * n
        for day, b in enumerate(bulbs):
            bulb_to_day[b-1] = day + 1

        min_queue = MinQueue(K)
        ans = math.inf
        for bulb, day in enumerate(bulb_to_day):
            min_queue.pop_expired(bulb)
            min_queue.push(day, bulb)
            if K <= bulb < len(bulb_to_day) - 1:
                left = bulb_to_day[bulb - K]
                right = bulb_to_day[bulb + 1]
                if min_queue.min() > (d := max(left, right)) or K == 0:
                    ans = min(ans, d)
        return ans if ans <= len(bulb_to_day) else -1

class MinQueue:
    def __init__(self, size):
        self.queue = deque()
        self.size = size

    def pop_expired(self, pos):
        if self.queue and pos - self.queue[0][1] >= self.size:
            self.queue.popleft()

    def push(self, x, pos):
        while self.queue and self.queue[-1][0] >= x:
            self.queue.pop()
        self.queue.append([x, pos])

    def min(self):
        return self.queue[0][0]