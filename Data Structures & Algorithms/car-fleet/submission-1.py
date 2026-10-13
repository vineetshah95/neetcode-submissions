class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #distance = speed * time 
        #time = distance/speed
        
        # 6/2 = 3
        # 9/2 = 4.5
        # 10/1 = 10
        # 3/1 = 3
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        stack = []
        k = 0
        for p,s in sorted(cars, reverse=True):
            time = (target - p) /s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                print(stack)
                stack.pop()
            k += 1
        return len(stack)