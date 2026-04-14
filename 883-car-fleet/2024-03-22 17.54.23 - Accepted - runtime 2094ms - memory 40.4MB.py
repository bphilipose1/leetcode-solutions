class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carArr = [[p,s] for p,s in zip(position, speed)]
        sortedCarArr = sorted(carArr, reverse = True)
        times = [(target - pos) / spd for pos, spd in sortedCarArr]
        fleet = 0
        while times:
            lead_time = times.pop(0)
            fleet+=1
            while times and times[0] <= lead_time:
                times.pop(0)
        
        return fleet

        