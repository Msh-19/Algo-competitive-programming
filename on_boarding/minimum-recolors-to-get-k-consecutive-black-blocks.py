class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        Min = float('inf')
        l = 0
        count = 0

        for r in range(len(blocks)):
            if blocks[r] == 'W':
                count += 1

            if r - l + 1 == k:
                Min = min(count,Min)
                if blocks[l] == 'W':
                    count -= 1
                l += 1
        
        return Min

                