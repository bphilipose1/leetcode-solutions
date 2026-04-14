class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carArr = [[p,s] for p,s in zip(position, speed)]
        sortedCarArr = sorted(carArr, reverse = True)
        stack = []
        for p,s in sortedCarArr:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()


        return len(stack)

        