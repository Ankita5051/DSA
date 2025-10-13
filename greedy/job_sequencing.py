import heapq
class Solution:
    def __init__(self,deadline,profit):
        self.deadline=deadline
        self.profit=profit

    def jobSequencingBYSorting(self): #time complexity -n^2 space complexity -n
        jobs=list(zip(self.deadline,self.profit))
        jobs.sort(key=lambda x:x[1],reverse=True)
        n=len(jobs)
        slot=[-1]*n

        job_count=0
        max_profit=0

        for i in jobs:
            for j in range(min(n,i[0]),-1,-1):
                if slot[j-1]==-1:
                    slot[j-1]=i
                    job_count+=1
                    max_profit+=i[1]
                    break
        return job_count,max_profit
    def jobSequencingBYDisjointSet(self): #time complexity -nlogn space complexity -n
        def find(slot,i):
            if slot[i]==-1:
                return i
            slot[i]=find(slot,slot[i])
            return slot[i]

        jobs=list(zip(self.deadline,self.profit))
        jobs.sort(key=lambda x:x[1],reverse=True)
        n=len(jobs)
        slot=[-1]*n

        job_count=0
        max_profit=0

        for i in jobs:
            available_slot=find(slot,min(n,i[0])-1)
            if available_slot>=0:
                slot[available_slot]=find(slot,available_slot-1)
                job_count+=1
                max_profit+=i[1]
        return job_count,max_profit
    
    def ByMinHeap(self):
        jobs= list(zip(self.deadline,self.profit))
        jobs.sort()

        min_heap=[]

        job_count=0
        profit=0
        for j in jobs:
            if j[0]>len(min_heap):
                heapq.heappush(min_heap,j[1])
            elif min_heap and min_heap[0]<j[1]:
                #replacing min profit of heap with new high profit
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,j[1])
        
        while min_heap:
            job_count+=1
            profit+= heapq.heappop(min_heap)
        
        return [job_count,profit]

        

def main():
    deadline=[4,1,1,1]
    profit =[2,100,38,102]

    schedular=Solution(deadline,profit)

    res=schedular.ByMinHeap()
    print(res)
if __name__ =='__main__':
    main()