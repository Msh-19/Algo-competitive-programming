class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = [deck[-1]]
        currIdx = len(deck) -2
        while len(ans) != len(deck):
            ans = [deck[currIdx]] + [ans[-1]] + ans[:-1]
            currIdx -= 1
        return ans