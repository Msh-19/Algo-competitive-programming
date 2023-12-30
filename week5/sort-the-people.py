class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combined = list(zip(names, heights))
    
        combined.sort(key=lambda x: x[1], reverse=True)
    
        sorted_names = [name for name, _ in combined]
        
        return sorted_names