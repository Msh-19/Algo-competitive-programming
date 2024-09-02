# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tot = 0
        for i in range(len(chalk)):
            tot += chalk[i]

            if tot > k:
                break
        k %= tot

        for j in range(len(chalk)):
            if k<chalk[j]:
                return j
            k-=chalk[j]
        return 0