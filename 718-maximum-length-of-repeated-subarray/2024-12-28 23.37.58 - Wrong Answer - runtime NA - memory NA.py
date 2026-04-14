class Solution:
    from collections import Counter
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #get the freqeuncy of each number in the array for both
        nums1.sort()
        nums2.sort()
        numFreqNums1 = Counter(nums1)
        numFreqNums2 = Counter(nums2)
        print(numFreqNums1, numFreqNums2)
        #take the min value of both values in teh dict, and sum them all together
        sum_res = 0
        for key in list(numFreqNums1.keys()):
            #check if it exists in other dict:
            if key in numFreqNums2:
                sum_res += min(numFreqNums1[key], numFreqNums2[key])
                del numFreqNums2[key] #remove from problem scope
                del numFreqNums1[key] #remove from problem scope
        
        for key in list(numFreqNums2.keys()):
            #check if it exists in other dict:
            if key in numFreqNums1:
                sum_res += min(numFreqNums2[key], numFreqNums1[key])
                del numFreqNums2[key] #remove from problem scope
                del numFreqNums1[key] #remove from problem scope
        return sum_res