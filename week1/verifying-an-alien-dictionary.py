class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {char: index for index, char in enumerate(order)}

        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            min_len = min(len(word1), len(word2))

            for j in range(min_len):
                if word1[j] != word2[j]:
                    if order_dict[word1[j]] > order_dict[word2[j]]:
                        return False
                    break
                elif j == min_len - 1 and len(word1) > len(word2):
                    return False

        return True