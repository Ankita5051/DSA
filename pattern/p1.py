'''
*****
*****
*****
*****
*****
'''
def pattern1(r,c):
    for i in range(r):
        for j in range(c):
            print('*',end='')
        print()
'''
*
**
***
****
*****
'''
def pattern2(r):
    for i in range(r):
        for j in range(i+1):
            print('*',end='')
        print()
'''
1
12
123
1234
12345
'''
def pattern3(r):
    for i in range(r):
        for j in range(i+1):
            print(j+1,end='')
        print()
'''
1
22
333
4444
55555
'''
def pattern4(r):
    for i in range(r):
        for j in range(i+1):
            print(i+1,end='')
        print()
'''
12345
1234
123
12
1
'''
def pattern5(r):
    for i in range(r,0,-1):
        for j in range(i):
            print(j+1,end='')
        print()
'''
    *
   ***
  *****
 *******
*********
'''
def pattern6(r):
    for i in range(r):
        for j in range(r+i):
            print(" ",end='') if j<r-i-1 else print("*",end='')
        print()
'''
*********
 *******
  *****
   ***
    *
'''    
def pattern7(r):
    for i in range(r):
        for j in range(2*r-i-1):
            print(" ",end='') if j<i else print("*",end='')
        print()
'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''
def pattern8(r):
    for i in range(r):
        if i<= r//2:
            k=r//2+i
        else:
            k-=1
        for j in range(k+1):
            if i<= r//2:
                print("*",end='') if j>=r//2 -i else print(" ",end='')
            else:
               
                print('*',end='') if j>=i-r//2 else print(" ",end='')
     
        print()
'''
*****
*   *
*   *
*   *
*****
'''
def pattern9(r):
    for i in range(r):
        for j in range(r):
            print('*',end='') if i==0 or i==r-1 or j==0 or j==r-1 else print(' ',end='')
        print()
'''
33333
32223
32123
32223
33333   
'''
#check again
def pattern10(n):
    r=2*(n-1)+1
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print(n,end='')
            elif i==1 or i==n-2 or j==1 or j==n-2:
                print(n-1,end='')
            elif i==2 or i==n-3 or j==2 or j==n-3:
                print(n-2,end='')
            else:
                print(n-3,end='')
        print()

def pattern11(n):
    r=2*n-1
    for i in range(r):
        if i<n:
            k=i+1
        else:
            k-=1
        for j in range(k):
            print('*',end='')
        print()
        
def pattern12(n):
    for i in range(1,n+1):
        for j in range(i):
            print((j+i)%2,end='')
        print()

def pattern13(n):
    pass

def main():
    pattern1(5,5)
    pattern2(5)
    pattern3(5)
    pattern4(5)
    pattern5(5)
    pattern6(5)
    pattern7(5)
    pattern8(7)
    pattern9(5)
    pattern10(5)
    pattern11(5)
    pattern12(5)
    pattern13(5)



if __name__ == '__main__':
    main()

