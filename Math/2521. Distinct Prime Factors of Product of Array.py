class Solution:
    def find_prime(self,n,prime_factor):
        i=2
        while i*i <= n:## if i*i<=n that means number is not prime otherwise number is prime
            while n%i ==0:
                prime_factor.add(i)
                n=n//i
            i+=1
        if n>1:
            prime_factor.add(n)

    def distinctPrimeFactors(self, nums: list[int]) -> int:
        prime_factor=set()
        for i in nums:
            self.find_prime(i,prime_factor)
        
        return len(prime_factor)

        