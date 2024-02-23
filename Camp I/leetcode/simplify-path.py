class Solution:
    def simplifyPath(self, path: str) -> str:
        components = list(path.split('/'))
        stack = []
        #print(components)
        for component in components:
            if component == '..':
                if stack: 
                    stack.pop()
            elif component == '.' or component == "":
                continue
            else:
                stack.append("/" + component)
        if len(stack) == 0:
            return "/"
            
        cannonical_path = ''.join(stack)
        return cannonical_path