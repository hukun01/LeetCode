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
        for base_name in names:
            final_name = base_name
            if base_name in created:
                while (final_name := f"{base_name}({created[base_name]})") in created:
                    created[base_name] += 1
                    final_name = f"{base_name}({created[base_name]})"
            created[final_name] = 1
            ans.append(final_name)
        return ans