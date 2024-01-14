class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:    
            return False
        index = self.val_to_index[val]      
        last_val = self.vals[-1]            
        self.vals[index] = last_val         
        self.val_to_index[last_val] = index 
        self.vals.pop()                     
        del self.val_to_index[val]           
        return True                          
    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()