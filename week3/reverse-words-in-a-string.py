class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        reversed = word[len(word)::-1]
        reversed = " ".join(reversed)
        return reversed