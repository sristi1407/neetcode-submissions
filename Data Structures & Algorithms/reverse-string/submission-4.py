class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack=[]
        i=0
        for c in s:
            stack.append(c)

        while stack:
            s[i]=stack.pop()
            i=i+1

        






       
     
  
        