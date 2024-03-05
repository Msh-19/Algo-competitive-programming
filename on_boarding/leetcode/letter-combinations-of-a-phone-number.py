class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        ans = []
        curr = []
        n = len(digits)

        def com(idx):
            if len(curr) == n:
                ans.append("".join(curr[:]))
                return

            if len(curr) >= n:
                ans.append(curr[:])
                return

            for seq in dic[digits[idx]]:
                curr.append(seq)
                com(idx + 1)
                curr.pop()

        com(0)
        if ans[0] == "":
            return []
        return ans
