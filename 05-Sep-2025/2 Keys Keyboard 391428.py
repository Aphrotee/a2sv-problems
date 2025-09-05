# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}
        
        if n <= 1:
            return 0

        def build(screen, clipb):
            if screen > n:
                return 1000
            if screen == n:
                return 1
            if (screen, clipb) in memo:
                return memo[(screen, clipb)]
            nextClipb = screen
            memo[(screen, clipb)] = min(1 + build(screen + clipb, clipb),
                               2 + build(screen + nextClipb, nextClipb))
            return memo[(screen, clipb)]
        
        return build(1, 1)