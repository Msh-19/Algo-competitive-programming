class Bitset:

    def __init__(self, size: int):
        self.bit_count = {"0":size,"1":0}
        self.bit_indexes = {"0":{i for i in range(size)},"1":set()}
        self.size = size
        
    def fix(self, idx: int) -> None:
        if idx in self.bit_indexes["1"]:
            return
        self.bit_indexes["0"].remove(idx)
        self.bit_indexes["1"].add(idx)
        self.bit_count["1"] = self.bit_count["1"] + 1
        self.bit_count["0"] = self.bit_count["0"] - 1
        

    def unfix(self, idx: int) -> None:
        if idx in self.bit_indexes["0"]:
            return
        self.bit_indexes["1"].remove(idx)
        self.bit_indexes["0"].add(idx)
        self.bit_count["1"] = self.bit_count["1"] - 1
        self.bit_count["0"] = self.bit_count["0"] + 1

    def flip(self) -> None:
        self.bit_indexes["0"],self.bit_indexes["1"] = self.bit_indexes["1"],self.bit_indexes["0"]
        self.bit_count["0"],self.bit_count["1"] = self.bit_count["1"],self.bit_count["0"]

    def all(self) -> bool:
        return self.bit_count["1"] == self.size

    def one(self) -> bool:
        return self.bit_count["1"] > 0

    def count(self) -> int:
        return self.bit_count["1"]

    def toString(self) -> str:
        res = ""
        for i in range(self.size):
            if i in self.bit_indexes["1"]:
                res+="1"
            else:
                res+="0"

        return res


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()