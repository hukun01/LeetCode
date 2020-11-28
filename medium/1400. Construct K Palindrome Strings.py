# 1400. Construct K Palindrome Strings
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        count = Counter(s)
        least = 0
        most = 0
        for v in count.values():
            if v % 2 == 1:
                least += 1
                most += v
            else:
                most += v
        return least <= k <= most