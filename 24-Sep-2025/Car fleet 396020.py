# Problem: Car fleet - https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)), key=lambda x: x[0])
        stack = [cars[-1]]
        n = len(speed)
        for i in range(n - 2, -1, -1):
            leftCar = cars[i]
            rightCar = stack[-1]
            timeLeftCar = self.get_time_to_target(target, leftCar[1], leftCar[0])
            timeRightCar = self.get_time_to_target(target, rightCar[1], rightCar[0])
            if timeLeftCar > timeRightCar:
                stack.append(leftCar)
        return len(stack)
        
    def get_time_to_target(self, target, carSpeed, currentPosition):
        return (target - currentPosition) / carSpeed
