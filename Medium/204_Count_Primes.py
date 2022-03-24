class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return 0

        primes = [1]*n
        primes[0] = primes[1] = 0

        for i in range(2,n):
            if primes[i]:

                for j in range(i+i,n,i):
                    primes[j] = 0

        return sum(primes)

if __name__ == "__main__":
    assert Solution().countPrimes(999999) == 78498
    assert Solution().countPrimes(10) == 4
    assert Solution().countPrimes(1) == 0
