class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lookup = defaultdict(int)
        winners = set()
        losers = set()

        for win, loss in matches:
            lookup[loss] +=1
            if win not in lookup:
                winners.add(win)

            if loss in winners:
                winners.remove(loss)

            if lookup[loss] == 1:
                losers.add(loss)
            else:
                if loss in losers:
                    losers.remove(loss)

        w = sorted(list(winners))
        l = sorted(list(losers))

        return [w,l]