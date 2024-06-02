# Problem: Find Building Where Alice and Bob Can Meet - https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n, m = len(heights), len(queries)
        nextGreater = [-1] * n
        stack = []
        result = []

        for i in range(m):
            queries[i].sort()
            queries[i].append(i)
        
        queries.sort(key=lambda x: x[1])
        j = len(queries) - 1

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()
            
            stack.append(i)

            while j >= 0 and i == queries[j][1]:
                alice, bob, index = queries[j]
                j -= 1

                if alice > bob:
                    alice, bob = bob, alice
                
                if alice == bob:
                    result.append((index, alice))
                    continue
                
                if heights[alice] < heights[bob]:
                    result.append((index, bob))
                    continue
                
                left, right = 0, len(stack) - 1

                while left <= right:
                    mid = (left + right) // 2
                    height = heights[stack[mid]]

                    if height > heights[alice]:
                        left = mid + 1
                    else:
                        right = mid - 1
                
                if right >= 0:
                    result.append((index, stack[right]))
                else:
                    result.append((index, -1))

        result.sort()
        return [val for ind, val in result]