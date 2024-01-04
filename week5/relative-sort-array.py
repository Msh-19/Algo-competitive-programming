class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = {}
        remaining = []
        result = []

        for num in arr1:
            counts[num] = counts.get(num,0) +1
            

        for num in arr2:
            if num in counts:
                result.extend([num]*counts[num])
                del counts[num]

        for num,count in counts.items():
            remaining.extend([num]*count)

        remaining.sort()
        result.extend(remaining)

        return result