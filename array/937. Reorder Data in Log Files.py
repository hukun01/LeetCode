class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Check log[1] to see if it's letter log or not,
        # retrieve the letter logs and digit logs;
        # Use sort(key=lambda x: (con1, con2)) to represent multiple attributes. Note that it's a tuple.
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