class Solution:
    def isOperand(self,ch):
        return True if ch>='a'and ch<='z' or ch>='A' and ch<='Z' or ch>='0' and ch<='9' else False
    def preToPost(self, pre_exp):
        # Code here
        st=[]
        for ch in pre_exp[::-1]:
            if self.isOperand(ch):
                st.append(ch)
            else:
                op1,op2=st[-1],st[-2]
                exp=op1+op2+ch
                st=st[:-2]
                st.append(exp)
                
        return st[-1]