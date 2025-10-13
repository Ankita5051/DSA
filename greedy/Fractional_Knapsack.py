class Solution:
    def __init__(self,values,weights,capacity):
        self.weights=weights
        self.values=values
        self.capacity=capacity
    
    def fractional(self):
      
        items=[(x/y,y) for x,y in zip(self.values,self.weights)]
        items.sort()
        n=len(items)

        c=self.capacity
        max_value=0
        while c and n:
            item=items[n-1]
            temp=min(c,item[1])
            max_value += item[0]*temp
            c-=temp
            n-=1
        return max_value

    