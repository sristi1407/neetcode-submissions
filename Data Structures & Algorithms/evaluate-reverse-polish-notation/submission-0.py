class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        opr = {'+','-','*','/'}

        for o in tokens:
            if o in opr:
                b = stack.pop()
                a = stack.pop()

                if o == '+':
                    stack.append(a + b)
                elif o == '-':
                    stack.append(a - b )
                elif o == '*':
                    stack.append(a * b)
                else: 
                    stack.append(int(a/b))

            else :
                stack.append(int(o))

        return stack[0]


