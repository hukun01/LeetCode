# 659. Split Array into Consecutive Subsequences
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        '''
        1/2 Greedy
        Keep track of remaining numbers that aren't used yet, and keep track of
        ending elements from each subsequence. As we go through the array, if
        an element 'a' can be added to any existing subsequence, we do so,
        because the only other thing we can do is to start a new subsequence
        that starts with 'a', and this does no good.
        If we add 'a' to an existing subseq, there must be at least 1 subseq
        ending at 'a-1', so we minus 1 from there, and add 1 for end[a].
        If we have to start a new subseq with 'a', check whether there's 'a+1'
        and 'a+2' in the remaining numbers, if so, consume them, update 
        remaining and end[a+2]; otherwise, return false.

        Time: O(n) where n is len(nums)
        Space: O(n)
        '''
        remain = Counter(nums)
        end = Counter()
        for a in nums:
            if remain[a] == 0:
                # used in advance previously
                continue
            remain[a] -= 1
            if end[a-1]:
                end[a-1] -= 1
                end[a] += 1
            elif remain[a+1] and remain[a+2]:
                remain[a+1] -= 1
                remain[a+2] -= 1
                end[a+2] += 1
            else:
                return False
        return True
        '''
        2/2 Greedy (more subtle but using constant space)
        Let 'pre' and 'cur' be the previous and current element, respectively.
        Let 'p1', 'p2', 'p3' be the number of subseqs that end at 'pre' with
        length being 1, 2, and >= 3, respectively.
        Two cases:
            1. cur == pre + 1:
                We can add cur to subseqs ending at 'pre', based on logic in
                1/2, we always do so when possible. Let 'c1', 'c2', 'c3' be
                similar numbers but for 'cur'. Few cases to check:
                    a. Ensure 'cur' count is at least 'p1 + p2', otherwise some
                       subseq can't extend to at least length 3. If there's
                       leftover, we can either add it to p3, or start new
                       subseqs. We never want to start new subseqs based on
                       logic in 1/2, so c1 = max(0, count - (p1 + p2 + p3)).
                    b. Based on case a, we know c2 = p1.
                    c. Finally, c3 has 2 parts, part1 is p2, p2 will add to
                       c3; part2 is from partial p3 and leftover 'cur' count,
                       depending on how many c3 remains after used by p1 and
                       p2, so it's part2 is min(p3, count - (p1 + p2)).
            2. cur != pre + 1:
                We can forget about subseqs ending at 'pre' now, all subseqs
                must now start from 'cur'. We just need to ensure p1 = p2 = 0.

        Time: O(n)
        Space: O(1)
        '''
        pre = -inf
        p1 = p2 = 0
        i = 0
        n = len(nums)
        while i < n:
            count = 1
            cur = nums[i]
            while i+1 < n and cur == nums[i+1]:
                count += 1
                i += 1
            if cur == pre + 1:
                if count < p1 + p2:
                    return False
                c1 = max(0, count - (p1 + p2 + p3))
                c2 = p1
                c3 = p2 + min(p3, count - (p1 + p2))
                p1 = c1
                p2 = c2
                p3 = c3
            else:
                if p1 or p2:
                    return False
                p1 = count
                p2 = p3 = 0
            pre = cur
            i += 1

        return p1 == p2 == 0