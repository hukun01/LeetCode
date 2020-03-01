class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        '''
        This is about having detailed control flow.
        Separate cases, don't handle them in one path.
        '''
        wIdx = 0
        lines = []
        while wIdx < len(words):
            wordsWidth = 0
            wordsCount = 0
            while wIdx < len(words) and wordsWidth + wordsCount + len(words[wIdx]) <= maxWidth:
                wordsWidth += len(words[wIdx])
                wIdx += 1
                wordsCount += 1
            line = []
            spacesCount = maxWidth - wordsWidth
            if wIdx < len(words):
                if wordsCount == 1:
                    line = words[wIdx - 1] + ' ' * spacesCount
                else:
                    line = words[wIdx - wordsCount: wIdx]
                    for i in range(spacesCount % (wordsCount - 1)): # evenly distribute extra spaces to left
                        line[i] += ' '
                    avgSpaces = spacesCount // (wordsCount - 1) # evenly distribute average spaces
                    line = (' ' * avgSpaces).join(line)
                lines.append(line)
        line = ' '.join(words[-wordsCount:])
        line += ' ' * (maxWidth - len(line))
        lines.append(line)
        return lines