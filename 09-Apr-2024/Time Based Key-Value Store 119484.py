# Problem: Time Based Key-Value Store - https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.structure = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.structure[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        temp = self.structure.get(key, [])
        low, high = 0, len(temp) - 1
        while low <= high:
            mid = (low + high) // 2
            if temp[mid][1] <= timestamp:
                ans = temp[mid][0]
                low = mid + 1
            else:
                high = mid -1

        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)