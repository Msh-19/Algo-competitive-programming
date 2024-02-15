class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billCount = defaultdict(int)

        state = True
        for bill in bills:
            billCount[bill] = 0
        
        
        for i in range(len(bills)):
            if bills[i] == 5:
                billCount[5] += 1

            elif bills[i] == 10:
                billCount[10] += 1
                if billCount[5] > 0:
                    billCount[5] -= 1
                else:
                    state = False

            elif bills[i] == 20:
                billCount[20] += 1
                if billCount[10] > 0 and billCount[5] > 0:
                    billCount[10] -= 1
                    billCount[5] -= 1
                elif billCount[10] < 1 and billCount[5] > 2:
                    billCount[5] -= 3
                else:
                    state = False
        return state