# 844. Backspace String Compare
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        '''
        Control flow.
        For string parsing problems, a key is to identify the exit condition,
        and use nested while loop to manage the inner condition transitions.
        '''
        def proceed(arr, idx):
            '''
            From right to left, find the index of the first char that is
            effectively present (would not be deleted).
            '''
            count = 0
            while idx >= 0 and (arr[idx] == '#' or count > 0):
                if arr[idx] == '#':
                    count += 1
                else:
                    count -= 1
                idx -= 1
            return idx

        s = proceed(S, len(S) - 1)
        t = proceed(T, len(T) - 1)
        while s >= 0 and t >= 0 and S[s] == T[t]:
            s -= 1
            t -= 1
            s = proceed(S, s)
            t = proceed(T, t)
        return s == t == -1