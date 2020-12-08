# 721. Accounts Merge
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        Union find.
        Name can be duplicate across different persons, so don't use it as
        a key. We can use email as a key because emails are unique. Let an
        email be a node in UF, we keep adding all emails under the same account
        entry. At the end some emails can be grouped from different account entries
        if they share some email.

        Time: O(n a) where n is the total number of emails we need to process, a is
        the inverse Ackermann function that can be treated as a constant.
        Space: O(n)
        '''
        uf = {}
        def find(node):
            if node != uf[node]:
                uf[node] = find(uf[node])
            return uf[node]

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            uf[p1] = p2

        email_to_name = {}
        for info in accounts:
            name = info[0]
            for email in info[1:]:
                email_to_name[email] = name
                if email not in uf:
                    uf[email] = email
                union(info[1], email)

        root_to_children = defaultdict(list)
        for child in uf:
            root_to_children[find(child)].append(child)

        return [[email_to_name[v[0]]] + sorted(v) for v in root_to_children.values()]