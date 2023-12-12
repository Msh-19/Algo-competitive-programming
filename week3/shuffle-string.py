class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        shuffled = [''] * len(s)

        for i, char in zip(indices,s):
            shuffled[i] = char

        return ''.join(shuffled)