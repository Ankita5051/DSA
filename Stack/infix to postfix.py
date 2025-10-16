# 1️     If operand - add it to result
# 2️     If '(' - push it to stack
# 3️     If ')' - pop from stack and add to result until '(' is popped
# 4️     If operator (except '^'):
#           While stack not empty and current op has lower/equal precedence than top of stack → pop and add to result
#           Then push current operator
#           ('^' is right-associative → pop only if precedence is strictly lower)
# 5️     After iteration → pop all remaining operators and add to result

class Solution:
    def isOperand(self,ch):
        if ch>='a' and ch<='z' or ch>='A' and ch<='Z' or ch>='0' and ch<='9':
            return True
        else:
            return False
    def precedence(self,op):
        if op=='^':
            return 3
        elif op=='*'or op=='/':
            return 2
        elif op=='+' or op=='-':
            return 1
        else:
            return 0
    def infixtoPostfix(self, s):
        #code here
        postfix=""
        st=[]

        for ch in s:
            #hadling operand
            if self.isOperand(ch):
                postfix+=ch
                continue
        
            #handing brackets
            if ch=='(':
                st.append(ch)
            elif ch==')':
                while st and st[-1]!='(':
                    postfix+=st[-1]
                    st.pop()
              
                st.pop()
            else:
                #handing operator
                if ch=='^':
                    while st and  self.precedence(ch)<self.precedence(st[-1]):#curr op have high periority then top of stack
                        postfix+=st[-1]
                        st.pop()
                else:
                    while st and  self.precedence(ch)<=self.precedence(st[-1]):#curr op have high periority then top of stack
                        postfix+=st[-1]
                        st.pop()
                    
                st.append(ch)
        while st:
            postfix+=st[-1]
            st.pop()
        return postfix
                
        
            
        
        