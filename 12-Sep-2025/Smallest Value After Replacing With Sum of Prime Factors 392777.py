# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        # prime_factors_sum = {1: 0}
        primes = self.get_primes(n)
        prime_set = set(primes)
        p = len(primes)
        ans = n

        if n == 4:
            return 4

        while ans not in prime_set:
            prime_f_sum = 0
            current_num = ans
            temp = 0
            i = 0
            fact = primes[i]
            while fact <= current_num and current_num > 1:
                fact = primes[i]
                if current_num % fact == 0:
                    # print(fact, temp)
                    temp += fact
                    current_num //= fact
                    # print(current_num, fact, temp)
                else:
                    i += 1
            # print(temp, current_num)
            ans = temp
        return ans

        
        # def get_sum_of_prime_factors(num):
        #     sum_factors = 0
        #     i = 2
        #     while i * i <= num:
        #         while num % i == 0:
        #             sum_factors += i
        #             num //= i
        #         i += 1
        #     if num > 1:
        #         sum_factors += num
        #     return sum_factors
        
        # curr_n = n
        # while True:
        #     next_n = get_sum_of_prime_factors(curr_n)
        #     if next_n >= curr_n:
        #         return curr_n
        #     curr_n = next_n

    
    def get_primes(self, num):
        primes = [True] * (num + 1)
        primes[0] = False
        primes[1] = False
        for factor in range(2, num + 1):
            if primes[factor]:
                step = factor
                for multiple in range(factor + factor, num + 1, step):
                    primes[multiple] = False
        return [prime for prime in range(2, num + 1) if primes[prime]]