class Solution:
    def isOperand(self,ch):
        return True if ch>='a' and ch<='z' or ch>='A'and ch<='Z' or ch>='0'and ch<='9' else False
    def postToPre(self, post_exp):
        # Code here
        st=[]
        for ch in post_exp:
            if self.isOperand(ch):
                st.append(ch)
            else:
                op1,op2=st[-1],st[-2]
                st=st[:-2]
                exp=ch+op2+op1
                st.append(exp)
        return st[-1]