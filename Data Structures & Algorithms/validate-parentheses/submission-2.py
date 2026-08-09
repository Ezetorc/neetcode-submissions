class Solution:
    def isValid(self, s: str) -> bool:
        depth = 0
        stack = []

        for char in s:
            if char == "(" or char == "[" or char == "{":
                depth += 1
                stack.append(char)
            elif len(stack) > 0:
                lastAdded = stack[-1]

                if ((char == ")" and lastAdded == "(") or
                   (char == "]" and lastAdded == "[") or 
                   (char == "}" and lastAdded == "{")):
                    depth -= 1
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return depth == 0


            