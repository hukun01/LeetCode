class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        '''
        '''
        wIdx = 0
        lines = []
        while wIdx < len(words):
            width = 0
            prevIdx = wIdx
            wordCount = wIdx - prevIdx
            while wIdx < len(words) and width + wordCount + len(words[wIdx]) <= maxWidth:
                width += len(words[wIdx])
                wIdx += 1
                wordCount = wIdx - prevIdx
            line = []
            delta = maxWidth - width
            if wIdx < len(words):
                avgSpaces = delta // max(wordCount - 1, 1)
                extraSpaces = delta % max(wordCount - 1, 1)
                while prevIdx < wIdx:
                    line.append(words[prevIdx])
                    line.append(' ' * (avgSpaces + min(1, extraSpaces)))
                    extraSpaces = max(0, extraSpaces - 1)
                    prevIdx += 1
                if len(line) > 2:
                    line.pop()
                lines.append(''.join(line))
        while prevIdx < len(words):
            line.append(words[prevIdx])
            if prevIdx != len(words) - 1:
                line.append(' ')
            prevIdx += 1
        line.append(' ' * (delta - (wordCount - 1)))
        lines.append(''.join(line))
        return lines