class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        numSet = nums[:]
        def recFunc(subset, numSet):
            #subset is what you have, and numset is what you can use

            #base case of a full array
            if len(subset) >= len(nums):
                result.append(subset[:])
            
            origNum = numSet[:]
            for index, x in enumerate(origNum):

                #include value permutation
                subset.append(x)     
                newNumSet = numSet[:index] + numSet[index+1:]
                recFunc(subset, newNumSet)
                
                # Backtrack
                subset.pop()
        recFunc([], nums)
        print(result)
        return result


                

