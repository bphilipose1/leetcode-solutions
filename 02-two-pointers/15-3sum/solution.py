class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        result = []
        for x, val in enumerate(sortedNums):
            if sortedNums[x-1] == val and x > 0:
                continue
            target = 0 - sortedNums[x]
            lPtr = x+1
            rPtr = len(nums) - 1
            while(lPtr < rPtr):
                tempval = sortedNums[lPtr] + sortedNums[rPtr]
                if tempval > target:
                    rPtr-=1
                elif tempval < target:
                    lPtr+=1
                else:
                    result.append([sortedNums[x], sortedNums[lPtr], sortedNums[rPtr]])
                    #ensure infinite loop doesnt persist
                    lPtr+=1
                    while lPtr < rPtr and sortedNums[lPtr-1] == sortedNums[lPtr]:
                        lPtr+=1
        return result


                

