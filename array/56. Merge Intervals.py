class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Two key points:
        1. sort by interval[0] is sufficient, no need to sort the second element in an interval
        2. the current[1] could be greater than the next[1], because current[0] < next[0], 
           such as [1,4] and [2, 3] should be merged into [1, 4]
        '''
        answer = []
        for i in sorted(intervals, key = lambda x: x[0]):
            if answer and answer[-1][1] >= i[0]:
                answer[-1][1] = max(i[1], answer[-1][1])
            else:
                answer.append(i)
                
        return answer