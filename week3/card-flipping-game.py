class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        output = set(fronts + backs)
        
        for i in range(len(fronts)):
            if fronts[i] == backs[i] and fronts[i] in output  :
                output.remove(fronts[i])
        if len(output) == 0:
            return 0
        return output.pop()
        


        