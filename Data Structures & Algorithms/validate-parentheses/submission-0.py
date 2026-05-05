class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis_stack = []
        for i in s:
            top = paranthesis_stack[-1] if len(paranthesis_stack) else None
            if i == "(" or i == "[" or i == "{":
                paranthesis_stack.append(i)
            elif i == ")":
                if top == "(":
                    paranthesis_stack.pop()
                else:
                    paranthesis_stack.append(i)
            elif i == "}":
                if top == "{":
                    paranthesis_stack.pop()
                else:
                    paranthesis_stack.append(i)
            elif i == "]":
                if top == "[":
                    paranthesis_stack.pop()
                else:
                    paranthesis_stack.append(i)
        
        return True if len(paranthesis_stack) == 0 else False