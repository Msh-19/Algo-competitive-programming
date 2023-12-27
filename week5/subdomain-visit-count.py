class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomain_counts = {}

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            subdomains = domain.split('.')

            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                if subdomain in subdomain_counts:
                    subdomain_counts[subdomain] += int(count)
                else:
                    subdomain_counts[subdomain] = int(count)

        result = [f"{count} {subdomain}" for subdomain,count in subdomain_counts.items()]
        return result