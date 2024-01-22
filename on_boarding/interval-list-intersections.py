class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if firstList == [] or secondList == []:
            return []

        i = 0
        j = 0
        ans = []

        while i < len(firstList) and j<len(secondList):
            l = max(firstList[i][0], secondList[j][0])
            r = min(firstList[i][1], secondList[j][1])
            if l <= r:
                ans.append([l,r])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return ans

