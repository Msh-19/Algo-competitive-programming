class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        peak_found = False
        peak_index = 0
        
        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i]:
                if not peak_found:
                    peak_index = i
                else:
                    return False
            elif arr[i - 1] > arr[i]:
                if peak_found:
                    continue
                else:
                    if peak_index != 0:
                        peak_found = True
                    else:
                        return False
            else:
                return False
        
        return peak_found and peak_index != 0 and peak_index != len(arr) - 1