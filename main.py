from greedy.Fractional_Knapsack import Solution as knapsack
from recursion.coin_change import solution as coin

def main():
    val=[60, 100, 120]
    wt=[10, 20, 30]
    k=knapsack(val,wt,50)
    max_val=k.fractional()
    print(max_val)

    coins=[1,2,3]
    sum=4
    c=coin(coins,sum)
    print(c.Byrecusion())

if __name__ == '__main__':
    main()