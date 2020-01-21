# 1024. Video Stitching
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        '''
        Similar to 45. Jump Game II, we keep track of an interval [begin, end],
        in which 'furthest' tracks the largest index we can reach from the
        *reachable, *continuous clips intervals that starts on or before 'curEnd'.
        
        From 'furthest' we start our next exploration in the continuous clips.
        
        We pick the furthest every time, the number of picks is the minimum number
        of clips that can stitch together to cover [0, T].
        '''
        ans = furthest = curEnd = 0
        i = 0
        clips.sort()
        while curEnd < T:
            while i < len(clips) and clips[i][0] <= curEnd:
                furthest = max(furthest, clips[i][1])
                i += 1
            if furthest == curEnd:
                return -1
            curEnd = furthest
            ans += 1
        return ans