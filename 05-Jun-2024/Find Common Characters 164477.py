# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word_size = len(words)
        result = []

        common = Counter(words[0])

        for i in range(1,word_size):
            currcommon = Counter(words[i])

            for lett in common.keys():
                common[lett] = min(common[lett],currcommon[lett])
        
        for lette,count in common.items():
            for _ in range(count):
                result.append(lette)

        return result
        
        