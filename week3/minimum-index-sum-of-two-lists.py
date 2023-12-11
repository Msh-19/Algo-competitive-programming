class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        sim = []
        

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    sim.append((list1[i], i, j))
            
        min_sum = min(sim, key = lambda x:x[1] + x[2])[1] +min(sim, key = lambda x:x[1] + x[2])[2]
        min_strings = [t[0] for t in sim if t[1] + t[2] == min_sum]
        return min_strings