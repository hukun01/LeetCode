# 1487. Making File Names Unique
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        '''
        Have a clear control flow.
        Fundamentals:
        1. don't change any base name, only append min counter to it.
        2. keep track of the largest counter that have been created.
        3. not only update the base name's counter, but also add all
           final names' counters.
        '''
        created = dict()
        ans = []
        for baseName in names:
            finalName = baseName
            if baseName in created:
                finalName = f"{baseName}({created[baseName]})"
                while finalName in created:
                    created[baseName] += 1
                    finalName = f"{baseName}({created[baseName]})"
            created[finalName] = 1
            ans.append(finalName)
        return ans