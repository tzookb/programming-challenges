from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mapper = Counter()

        for domain_data in cpdomains:
            [count, domain] = domain_data.split(" ")
            parts = domain.split(".")
            count = int(count)

            for idx in range(len(parts)):
                cur_domain = ".".join(parts[idx:])
                mapper[cur_domain] += count
        
        final = []
        for subdomain in mapper:
            cnt_val = mapper[subdomain]
            final.append("%s %s" % (cnt_val, subdomain))

        return final
