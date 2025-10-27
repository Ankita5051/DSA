#question:  https://leetcode.com/discuss/post/5894381/amazon-oa-question-by-anonymous_user-eavm/


def solve(b:str,arr:list):
    res=[False]*len(arr)
    for i in range(len(arr)):
        target=list(arr[i])
        cnt0=b.count('0')
        cnt1=b.count('1')
        for i in range(len(b)):
            if target[i]=='?':
                if cnt0>0:
                    target[i]='0'
                    cnt0-=1
                else:
                    target[i]='1'
                    cnt1-=1

            else:
                if target[i]=='1':
                    cnt1-=1
                else:
                    cnt0-=1
        if cnt0<0 or cnt1<0:
            break
        if cnt0 !=0 or cnt1!=0:
            break

        need_zer=0
        for i in range(len(b)-1,-1,-1):
            if b[i]==0:
                need_zer+=1
            if target[i]==0:
                need_zer-=1
                if need_zer<0:
                    break
        res[i]=True
    
    return res

# b="101100"
# arr=["?110?1","111???"]
      
# print(solve(b,arr))