# You are given a lowercase string s of length n.
# For each length l (where 1 ≤ l ≤ n), find the lexicographically largest subsequence of s having exactly l characters.
def getsubseq(s):
    n=len(s)
    result=[]
    for l in range(1,n+1):
        rm=n-l
        st=[]
        for c in s:
            while st and rm and st[-1]<c:
                st.pop()
                rm-=1
            st.append(c)
        result.append("".join(st[:l]))
    return result
