#imp rotate tech
# for rotate(s,b)  s='abcdef' b=2  op=efabcd
#reverse(begin(s),end(s))
#reverse (begin(S),begin(s)+b)
#reverse(begin(s)+b,end(s))



class Solution:
    def rotate(self,s,b):
        s=s[::-1]
        s=s[:b][::-1] + s[b:]
        s=s[:b] + s[b:][::-1]
        return s
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        res=s
        que=[s]
        visited=set()
        visited.add(s)
        while que:
            curr=que[0]
            que.pop(0)
            if curr< res:
                res=curr
            #add a
            temp= list(curr)
            for i in range(1,len(temp),2):
                temp[i]=chr((int(temp[i])+a)%10 + ord('0'))
            temp="".join(temp)
         
            if temp not in visited:
                visited.add(temp)
                que.append(temp)
            #rotate b time
            temp=curr
            temp=self.rotate(temp,b)
        
            if temp not in visited:
                visited.add(temp)
                que.append(temp)
      
        return res
        