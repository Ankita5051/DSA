def solve(k,reward_1,reward_2):
    n=len(reward_1)
    tasks=[]
    for i in range(n):
        gain=reward_1[i]-reward_2[i]
        tasks.append((gain,reward_1[i],reward_2[i]))

    tasks.sort(reverse=True,key=lambda x:x[0])
    total=0
    for i in range(n):
        if i<k:
            total+=tasks[i][1]
        else:
            total+=tasks[i][2]
    print(total)
k=3
reward_2=[1,2,3,4,5]
reward_1=[5,4,3,2,1]
solve(k,reward_1,reward_2)
