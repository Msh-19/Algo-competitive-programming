class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        rt = []
        li = list(s)

        for i in range(len(s)):
            if li[i] == "(":
                stack.append("(")

            elif stack and li[i] == ")":
                val = 0
                if not str(stack[-1]).isdigit():
                    stack.pop()
                    stack.append(1)
                    continue
                    
                while str(stack[-1]).isdigit():
                    val += stack.pop()
                    
                stack.pop()
                stack.append(2*val)

        #print(stack)
        return sum(stack)
