# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [1] * n
        if n <= 2 :
            return 0
        is_prime[0] = 0
        is_prime[1] = 0

        for factor in range(2, n):
            if is_prime[factor] == 1:
                for multiple in range(factor * factor, n, factor):
                    is_prime[multiple] = 0
        return sum(is_prime)