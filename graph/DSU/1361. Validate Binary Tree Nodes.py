#each child can have eaxcly 1 parent
#no cycle
#connected component
class Solution:
    def find(self,x,parent):
        if x==parent[x]:
            return x
        else:
            parent[x]=self.find(parent[x],parent)
            return parent[x]
    def union(self,x,y,parent):
        x_par=self.find(x,parent)
        y_par=self.find(y,parent)
        
        if y_par != y:
            return True #child have 2 parent
        if x_par==y_par:
            return True #cycle exist cause parent and child belongs to same set
    
        parent[y_par]=x_par
        return False
        

    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        parent=[i for i in range(n)]
        comp=n
        for i in range(n):
            lc=leftChild[i]
            if  lc != -1:
               
                if self.union(i,lc,parent):
                    return False
                else:
                    comp-=1
        
        for i in range(n):
            rc=rightChild[i]
            if rc != -1:
               
                if self.union(i,rc,parent):
                    return False
                else:
                    comp-=1
  
        return True if comp==1 else False
            
        