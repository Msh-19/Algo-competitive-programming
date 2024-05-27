# Problem: B - String Fusion - https://codeforces.com/gym/526229/problem/B

# def collapse_length(a, b):
#     stack = list(a)
    
#     for char in b:
#         if stack and stack[-1] == char:
#             stack.pop()
#         else:
#             stack.append(char)
    
#     return len(stack)

# def solve(n, strings):
#     total_length = 0
    
#     for i in range(n):
#         for j in range(n):
#             total_length += collapse_length(strings[i], strings[j])
    
#     return total_length


# import sys
# input = sys.stdin.read
# data = input().split()

# n = int(data[0])
# strings = data[1:]

# result = solve(n, strings)

# print(result)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        cur = self.root
        for c in word:
            ind = ord(c) - ord("a")
            
            if ind not in cur.children:
                cur.children[ind] =TrieNode()
            
            cur = cur.children[ind]
            cur.count += 1

    def search(self, word):
        curr= self.root
        ans = 0
        for c in word:
            ind = ord(c) - ord("a")
            if ind not in curr.children:
                return ans
            
            curr = curr.children[ind]
            ans += curr.count*2
            
        return ans
                

n = int(input())
s = [input() for i in range(n)]
trie = Trie()
for cur in s:
	trie.insert(cur)
total = sum([len(cur)*2*n for cur in s])
for cur in s:
	total -= trie.search(cur[::-1])
print(total)

                