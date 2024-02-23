class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        curr = 0
        ops = 0

        while maxDoubles > 0 and target>1:
            if target%2 != 0:
                target = (target-1)
                ops += 1
                continue
            else:
                target//=2
                ops += 1
                maxDoubles -= 1

        ops += target-1
        
        return ops
            