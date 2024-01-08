class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        output = []

        while n>1:
            max_idx = arr.index(max(arr[:n]))
            if max_idx != n-1:
                output.append(max_idx + 1)
                arr[:max_idx + 1] = arr[:max_idx + 1][::-1]

                output.append(n)
                arr[:n] = arr[:n][::-1]
        
            n-=1

        return output