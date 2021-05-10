# 1130. Minimum Cost Tree From Leaf Values
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        '''
        1/2 Greedy.

        Each time we use two leaves, the smaller leaf wouldn't get used
        anymore, so essentially we pay a*b cost to remove 'a', where 'a <= b'.

        To have the min product from non-leaf node, we need to use the min
        leaves as early as possible. In another word, we try to put the greater
        numbers as high as possible, so they have smaller impact to the answer.

        Until arr gets to one element, we find the min element 'a' in each
        iteration, and to use it, we find the smaller one of the greater
        neighbors from left and right, this is the 'b'. Now we add 'a*b', and
        pop(a).

        Time: O(n^2) where n is len(arr), we need O(n) time to iterate, in each
              iteration, we use another O(n) time to find and remove 'a'.
        Space: O(n)
        '''
        ans = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            ans += min(arr[i-1:i] + arr[i+1:i+2]) * arr.pop(i)

        return ans
        '''
        2/2 Monotonic decreasing stack.

        We don't need the global min every time, instead, we use a leaf if
        it's smaller than next element. We are looking for the next greater
        element. Use a stack to track the smallest elements so far, when the
        current element is greater than the ones in stack, we can use the local
        min leaf in stack. As the cost is 'a * b', we pop the min leaf out as
        'a', and to pick 'b', we take the min of 'stack[-1]' and 'cur'.

        After this process, we have used all the min leaves that have next
        greater elements on their right side. Now we need to use the remaining
        leaves in stack, those leaves have the next greater elements on their
        left, so we just pop out each one as 'a', and 'b' is just stack[-1].
        We only do this when the tree has at least 2 nodes, aka, when
        len(stack) > 2 (considering the sentinel value).

        Note that a trick to make logic concise is to have a sentinel value in
        stack as inf, which would never be picked as 'b' or trigger the process.

        Time: O(n)
        Space: O(n)

        Similar to 503. Next Greater Element II.
        '''
        ans = 0
        stack = [inf]
        for cur in arr:
            while stack[-1] <= cur:
                mid = stack.pop()
                ans += mid * min(stack[-1], cur)
            stack.append(cur)

        while len(stack) > 2:
            ans += stack.pop() * stack[-1]

        return ans