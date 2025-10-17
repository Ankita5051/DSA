class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        n=len(colors)
        res=0
        wind=1
        for i in range(1,n+k-1):
            pre=(i-1)%n
            curr=i%n
         
            if colors[pre] != colors[curr]:
                wind+=1
                if wind>=k:
                    res+=1
                    wind-=1
            else:
                wind=1
            
        return res