class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #start with bound of our search space
        l, r = 1, max(piles)

        #keep searching till l and r agree or converge
        result = max(piles)
        while l <= r:
            temp_eat_rate = (r + l) // 2

            #check how many hours it takes with temp_eat_rate
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / temp_eat_rate) #gets the total hours needed, rounded to next whole hour
            
            
            #if the hours takes more than h limit, we need to up the rate, so lets do l = temp_eat_rate, else we will do r = temp_eat_rate to see if we can do lower rate
            if hours > h:
                l = temp_eat_rate + 1
            else:
                result = temp_eat_rate
                r = temp_eat_rate - 1

        
        return result