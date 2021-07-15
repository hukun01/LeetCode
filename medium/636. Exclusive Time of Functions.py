# 636. Exclusive Time of Functions
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        '''
        Use a stack to keep track of the function id that's currently running.

        Let 'pre' be the start time of the previous interval.
        When we see a start, if the stack is empty, this is the first function;
        otherwise, the current function's time should add (time - pre), and
        new function id should be pushed into stack, and pre will be updated to
        current time.
        When we see an end, we know the current function id in the stack peek has
        ended, we add the function's time by (time - pre + 1), and update pre to
        be (time + 1), because we need to avoid adding the previous interval more
        than once if there are functions that started earlier than the current ending
        function.

        Time: O(L) where L is len(logs)
        Space: O(n)
        '''
        ans = [0] * n
        logs = [log.split(':') for log in logs]
        cur_ids_stack = []
        pre = 0
        for i, op, t in logs:
            time = int(t)
            if op == "start":
                if cur_ids_stack:
                    ans[cur_ids_stack[-1]] += time - pre
                cur_ids_stack.append(int(i))
                pre = time
            else:
                ans[cur_ids_stack.pop()] += time + 1 - pre
                pre = time + 1

        return ans