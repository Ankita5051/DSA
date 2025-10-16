#1 reverse string handle brackets
#2 find postfix
#3 reverse the postfix
class Solution:
    def isOperand(self,ch):
        if ch>='a' and ch <='z' or ch>='0' and ch<='9' or ch>='A' and ch<='Z':
            return True
        else:
            return False
    def precedence(self,ch):
        if ch=='^':
            return 3
        elif ch=='*' or ch=='/':
            return 2
        elif ch=='+' or ch=='-':
            return 1
        else:
            return 0
  
        
    def infixToPrefix(self, s):
        #code here
        s=s[::-1] #reverse
        #find postfix
        res=''
        st=[]
        for ch in s:
            #handling operand
            if self.isOperand(ch):
                res+=ch
            elif ch==')':
                st.append(ch)
            elif ch=='(':
                while st and st[-1]!=')':
                    res+=st[-1]
                    st.pop()
                
                st.pop()
            else:
                #handling operator
                if ch=='^':
                    while st and self.precedence(ch)<=self.precedence(st[-1]):
                        res+=st[-1]
                        st.pop()
                else:
                    while st and self.precedence(ch)<self.precedence(st[-1]):
                        res+=st[-1]
                        st.pop()
                st.append(ch)
        while st:
            res+=st[-1]
            st.pop() 
        return res[::-1]# reverse and return
                    
        
# s=a+b*(c^d-e)^(f+g*h)-i
# s=h^m^q^(7-1)  
        
        