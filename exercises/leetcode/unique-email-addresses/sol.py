from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = self.groupByDomains(emails)
        print(res)
        total = self.countUniqueEmails(res)
        print(total)

    def countUniqueEmails(self, domainsEmails) -> int:
        total = 0

        for domain in domainsEmails:            
            total += len(domainsEmails[domain])

        return total

    def cleanEmailName(self, email: str) -> str:
        email = email.replace(".", "")
        emailChunks = email.split("+")
        return emailChunks[0]

    def groupByDomains(self, emails: List[str]) -> int:
        domains = {}

        for email in emails:
            name, domain = email.split("@")
            if domain not in domains:
                domains[domain] = {}

            clean_email = self.cleanEmailName(name)
            domains[domain][clean_email] = True

        return domains

emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
s = Solution()
s.numUniqueEmails(emails)