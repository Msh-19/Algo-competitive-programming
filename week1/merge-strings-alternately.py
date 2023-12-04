class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = ""
        remainder = ""
        if len(word1) < len(word2):
            remainder = word2[len(word1):]
        elif len(word2) < len(word1):
            remainder = word1[len(word2):]
        for i in range(min(len(word1),len(word2))):
            merge += word1[i]
            merge += word2[i]
        merge += remainder
        return merge