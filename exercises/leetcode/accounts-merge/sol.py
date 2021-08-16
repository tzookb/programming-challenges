from typing import List
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph, email_to_name_mapping = self.getGraphAndNameMapper(accounts)
        results = []
        visited = {}

        for ele in graph:
            if ele in visited:
                continue

            email_owner_name = ''
            queue = [ele]
            curRes = []

            while queue:
                node = queue.pop(0)
                if node in visited:
                    continue

                if isinstance(node, str):
                    email_owner_name = email_to_name_mapping[node]
                    curRes.append(node)

                for child in graph[node]:
                    queue.append(child)

                visited[node] = True

            curRes.sort()
            curRes = [email_owner_name] + curRes
            results.append(curRes)

        return results

    def getGraphAndNameMapper(self, accounts: List[List[str]]):
        email_to_name_mapping = {}
        graph = {}
        
        for idx, account_data in enumerate(accounts):
            username = account_data[0]
            graph[idx] = {}
            for email in account_data[1:]:
                graph[idx][email] = True
                if email not in graph:
                    graph[email] = {}
                graph[email][idx] = True

                email_to_name_mapping[email] = username
        return (graph, email_to_name_mapping)

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
s = Solution()
s.accountsMerge(accounts)