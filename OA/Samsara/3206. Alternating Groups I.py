class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        n=len(colors)
        res=0
        for i in range(n):#treat i as mid index
            left=(i-1)%n
            right=(i+1)%n
            if colors[i]!= colors[left] and colors[i]!=colors[right]:
                res+=1
        return res