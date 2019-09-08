class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Check log[1] to see if it's letter log or not,
        # retrieve the letter logs and digit logs;
        # Use sort(key=lambda x: condition1, condition2) to sort with additional tie-breaking condition2
        letterLogs = []
        digitLogs = []
        for log in logs:
            words = log.split(' ')
            if words[1].isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append(log)
        letterLogs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letterLogs + digitLogs