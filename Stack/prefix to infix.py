class Solution:
    def isOperand(self,ch):
        if ch>='a' and ch<='z' or ch>='A' and ch<='Z' or ch>='0' and ch<='9':
            return True
        return False
    def preToInfix(self, pre_exp):
        # Code here
        st=[]
        for ch in pre_exp[::-1]:
            #handing operand
      
            if self.isOperand(ch):
                st.append(ch)
            else:
                op1,op2=st[-1],st[-2]
                st.pop()
                st.pop()
                exp='('+op1+ch+op2+')'
          
                st.append(exp)
            
                
        return st[-1]
    
#     *-A/BC-/AKL
# -+a*b^-^cde+f*ghi
# ^h^m^q-71
                