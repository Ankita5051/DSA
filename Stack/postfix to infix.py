#1.just apply prefix to postfix
#2.handle brackets returned the reversed expression

class Solution:
    def isOperand(self,ch):
        if ch>='a'and ch<='z' or ch>='A' and ch<='Z' or ch>='0' and ch<='9':
            return True
        return False
        
    def postToInfix(self, postfix):
        # Code here
        
        st=[]
        for ch in postfix:
            if self.isOperand(ch):
                st.append(ch)
            else:
                op1,op2=st[-1],st[-2]
                st=st[:-2]
                exp=')'+op1+ch+op2+'('
                st.append(exp)
                
        return st[-1][::-1]
    
