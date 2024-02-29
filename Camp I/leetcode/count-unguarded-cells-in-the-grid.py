class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def goLeft(i, j):
            if j < 0 or (i, j) in walls or (i, j) in guards:
                return
            seen.add((i, j))
            goLeft(i, j - 1)
        def goRight(i, j):
            if j >= n or (i, j) in walls or (i, j) in guards:
                return
            seen.add((i, j))
            goRight(i, j + 1)
        def goBottom(i, j):
            if i >= m or (i, j) in walls or (i, j) in guards:
                return
            seen.add((i, j))
            goBottom(i + 1, j)
        def goUp(i, j):
            if i < 0 or (i, j) in walls or (i, j) in guards:
                return
            seen.add((i, j))
            goUp(i - 1, j)
        walls = set((i, j) for i, j in walls)
        guards = set((i, j) for i, j in guards)
        seen = set()
        for i, j in guards:
            goLeft(i, j - 1)
            goRight(i, j + 1)
            goBottom(i + 1, j)
            goUp(i - 1, j)
        return (m * n) - len(walls) - len(guards) - len(seen)
