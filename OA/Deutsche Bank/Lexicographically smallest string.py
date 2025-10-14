from collections import defaultdict
def solve(string:str,arr:list)->str:
    map=defaultdict(list)#"weight:string"
    n=len(arr)
    for st,i in zip(string,arr):
        map[i].append(st)
    for k in map:
        map[k].sort()
  
    res=[]
    for i in arr:
        res.append(map[i].pop(0))
    return ''.join(res)


if __name__=='__main__':
    string="xvrb"
    arr=[2,1,2,2]#weights for each char in string if weights are equal only then they can be swaped
    lss=solve(string,arr)
    print(lss)