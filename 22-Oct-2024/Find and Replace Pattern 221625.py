# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # count = Counter(pattern)
        # res = []
        # for i in words:
        #     countw = Counter(i)
        #     if len(countw) == len(count):
        #         res.append(i)
        
        # return res
        def helper(s):
            mapping = dict()
            for character in s:
                if character not in mapping:
                    mapping[character] = str(len(mapping))
            return ".".join(map(mapping.get,s))
        
        patter_string = helper(pattern)

        return [word for word in words if helper(word) == patter_string]