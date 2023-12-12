class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        bpivot = [x for x in nums if x>pivot]
        lpivot = [x for x in nums if x<pivot]
        pivotp = [x for x in nums if x == pivot]
        output = []
        
        lpivot.extend(pivotp)
        lpivot.extend(bpivot)
        return lpivot
        
            
        
