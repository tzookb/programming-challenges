from typing import List
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        connections_graph = self.createGraph(accounts)
        email_to_username_mapper = self.getEmailToUsernameMapper(accounts)
        groups = self.getEmailGroups(connections_graph)

        final = []
        for group in groups:
            group.sort()
            username = email_to_username_mapper[group[0]]
            final.append(
                [username] + group
            )

        return final

    def getEmailGroups(self, connections_graph):
        visited = {}
        all_groups = []
        to_process = list(connections_graph.keys())
        for email in to_process:

            cur_group = []
            group_queue = [email]
            while group_queue:
                cur = group_queue.pop(0)
                if cur in visited:
                    continue
                visited[cur] = True
                connected_emails = list(connections_graph[cur].keys())
                group_queue += connected_emails
                cur_group.append(cur)
            
            all_groups.append(cur_group)

        filtered = list(filter(lambda group: group, all_groups))
        return filtered

    def getEmailToUsernameMapper(self, accounts: List[List[str]]):
        mapper = {}
        for account_data in accounts:
            username = account_data[0]
            emails = account_data[1:]
            for email in emails:
                mapper[email] = username
        return mapper

    def createGraph(self, accounts: List[List[str]]):
        graph = {}
        for account_data in accounts:
            emails = account_data[1:]
            for i in range(len(emails)):
                cur_email = emails[i]
                if cur_email not in graph:
                        graph[cur_email] = {}
                for j in range(i + 1, len(emails)):
                    connected_email = emails[j]
                    if connected_email not in graph:
                        graph[connected_email] = {}
                    graph[cur_email][connected_email] = True
                    graph[connected_email][cur_email] = True
        return graph

accounts = [
    ["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","johnsmith@mail.com","john00@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
]

s = Solution()
res = s.accountsMerge(accounts)
print(res)