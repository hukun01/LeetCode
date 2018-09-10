class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]

        Store the index in a stack, when seeing a new temperature, if the last temperature in stack is lower, 
        pop that out and mark that index distance as the answer at the last index; otherwise, keep it 0.
        """
        stack = [] # store the INDEX
        ans = [0 for i in temperatures]
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                idx = stack.pop() # each idx would be accessed ONCE at most
                ans[idx] = i - idx
            stack.append(i)
        return ans