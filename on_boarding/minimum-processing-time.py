class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)

        l = 0
        output = 0

        for i in processorTime:
            cur = 0
            cnt = 0
            while l<len(tasks) and cnt < 4:
                cur = max(cur,i+tasks[l])
                l+=1
                cnt+=1
            output = max(output,cur)
        return output