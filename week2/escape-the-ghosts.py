class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        d = abs(target[0]) + abs(target[1])

        for ghost in ghosts:
            distance = abs(target[0]-ghost[0]) + abs(target[1]-ghost[1])

            if distance <= d:
                return False
        return True