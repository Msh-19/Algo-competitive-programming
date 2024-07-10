# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for curr in logs:
            if curr == "../":
                count = max(0,count-1)
            elif curr != "./":
                count += 1
        
        return count