class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def recFunc(index):
            #base case where the subset cant include or exclude another number
            if index >= len(nums):
                result.append(subset[:])
                return


            #case where we dont include the value in the subset
            recFunc(index + 1)

            #case where we include the value in the subset
            subset.append(nums[index])
            recFunc(index + 1)

            subset.pop()           
            
            return
        
        recFunc(0)
        return result
                    