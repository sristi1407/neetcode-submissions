class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        match = {')':'(' , '}': '{' , ']':'['}

        for brackets in s :
            if brackets in match.values():
                stack.append(brackets)

            else :
                if not stack or stack.pop() != match[brackets]:
                    return False

        return not stack
