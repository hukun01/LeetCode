# 1024. Video Stitching
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        '''
        1/2 No sort(), but use bucket sort.
        We only pick the largest end for each start, and within the current end,
        we can pick the clip that takes us to the furthest.
        Only after that we need to pick a new clip.
        This solution relies on the fact that T is relatively small, because we need
        O(T) space and O(max(N, T)) time.
        '''
        ends = [0] * (T + 1)
        for s, e in clips:
            if s <= T:
                ends[s] = max(ends[s], min(e, T))
        i = ans = furthest = curEnd = 0
        while curEnd < T:
            while i <= curEnd:
                furthest = max(furthest, ends[i])
                i += 1
            if furthest == curEnd:
                return -1
            curEnd = furthest
            ans += 1
        return ans

        '''
        2/2 Sorting
        Similar to 45. Jump Game II, we keep track of an interval [begin, end],
        in which 'furthest' tracks the largest index we can reach from the
        *reachable, *continuous clips intervals that starts on or before 'curEnd'.
        
        From 'furthest' we start our next exploration in the continuous clips.
        
        We pick the furthest every time, the number of picks is the minimum number
        of clips that can stitch together to cover [0, T].
        '''
        i = ans = furthest = curEnd = 0
        clips.sort()
        while curEnd < T:
            while i < len(clips) and clips[i][0] <= curEnd:
                furthest = max(furthest, clips[i][1])
                i += 1
            if furthest == curEnd:
                # we are not advancing, can't stitch up to T.
                return -1
            curEnd = furthest
            ans += 1
        return ans