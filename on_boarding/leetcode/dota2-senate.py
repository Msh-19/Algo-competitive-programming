class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dires = deque()
        radiants = deque()


        for pos,party in enumerate(senate):
            if party == "D":
                dires.append(pos)
            if party == "R":
                radiants.append(pos)

        if len(senate) == 1:
            return "Dire" if senate == "D" else "Radiant"

        count = len(senate)
        while dires and radiants:
            if radiants[0] < dires[0]:
                radiants.append(count)
            else:
                dires.append(count)

            radiants.popleft()
            dires.popleft()
            count+=1

        return "Radiant" if radiants else "Dire"