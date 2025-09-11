# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        maxi = max(nums)
        product = nums[0]
        for i in range(1, n):
            product *= nums[i]
        primes = self.get_primes(maxi)

        for prime_factor in primes:
            if product % prime_factor == 0:
                ans += 1

        return ans
    
    def get_primes(self, n):
        if n < 2:
            return []
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for num in range(2, n + 1):
            if is_prime[num]:
                factor = num
                step = num
                for multiple in range(factor + step, n + 1, step):
                    is_prime[multiple] = False
                
        return set([prime for prime in range(n + 1) if is_prime[prime]])