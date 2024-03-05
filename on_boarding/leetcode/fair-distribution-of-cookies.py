class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        curr = [0]*k
        n = len(cookies)
        def dfs(i,zero_count):
            if n - i < zero_count:
                return inf

            if i == n:
                return max(curr)

            answer = inf
            for j in range(k):
                zero_count -= int(curr[j] == 0)
                curr[j] += cookies[i]
                
                # Recursively distribute the next cookie.
                answer = min(answer, dfs(i + 1, zero_count))
                
                curr[j] -= cookies[i]
                zero_count += int(curr[j] == 0)
            
            return answer

        return dfs(0,k)
        