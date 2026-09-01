class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        '''
        This is about having detailed control flow.
        Separate cases, don't handle them in one path.

        A line can fit x words if sum(len(x)) + x - 1 <= maxWidth
        When maxWidth < sum(len(x + 1)) + (x + 1 - 1), aka, can't fit the next word, 
        the extraSpaces in the current line = maxWidth - (sum(len(x)) + x - 1).

        Note that when checking the boundary of a line, we need to check sum_len_x + len(words[w_i + x]) + "x" <= maxWidth,
        instead of sum_len_x + len(words[w_i + x]) + "x - 1" <= maxWidth, because x is the current number of words, and
        we are looking to add the next word, so it's actually "x + 1 - 1".
        
        If this is the last line, we put all the extra spaces at the end of the line.
        Otherwise, we distribute the extra spaces in two steps:
        1. for all words in this line: extraSpaces // (x - 1)
        2. for left words, add one space until we exhaust extraSpaces % (x - 1)
        '''
        w_i = 0
        x = 0
        while w_i < len(words):
            sum_len_x = len(words[w_i])
            x = 1
            while w_i + x < len(words) and sum_len_x + len(words[w_i + x]) + x <= maxWidth:
                sum_len_x += len(words[w_i + x])
                x += 1
            extra_spaces = maxWidth - (sum_len_x + x - 1)
            if x - 1 == 0:
                ans.append(words[w_i] + ' ' * extra_spaces)
            else:
                # if it is last line, then left-justified
                if w_i + x == len(words):
                    line = ' '.join(words[w_i:]) + ' ' * extra_spaces
                    ans.append(line)
                else:
                    all_w_spaces = extra_spaces // (x - 1)
                    remaining_spaces = extra_spaces % (x - 1)
                    line = []
                    for i in range(x - 1):
                        if remaining_spaces > 0:
                            remaining_spaces -= 1
                            line.append(words[w_i + i] + ' ' * (all_w_spaces + 1))
                        else:
                            line.append(words[w_i + i] + ' ' * all_w_spaces)
                    line.append(words[w_i + x - 1])
                    ans.append(' '.join(line))
            w_i += x

        return ans
