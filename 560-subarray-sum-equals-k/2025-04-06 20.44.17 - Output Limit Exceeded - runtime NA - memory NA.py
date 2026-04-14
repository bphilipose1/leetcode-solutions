class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # create the prefix sum array
        result_pairs = 0
        cur_sum = 0
        t_dict = {}
        for idx, val in enumerate(nums):
            #for each prefix sum store in dictionary and count what index they are at
            #find number of possible pairs
            cur_sum += val
            if cur_sum == k:
                print('hit at ', idx)
                result_pairs += 1
            
            #keep checking the rest in case a 0 exists
            
            target_compliment_val = cur_sum - k
            if target_compliment_val in t_dict:
                print('hit at, ', idx, len(t_dict[target_compliment_val]) )
                #at each new prefix added, find complementary pairs 
                #all possible compliments
                result_pairs += len(t_dict[target_compliment_val]) 
        
            
            
            
            if cur_sum in t_dict:
                t_dict[cur_sum].append(idx)
            else:
                t_dict[cur_sum]=[idx]
            print(t_dict)
            
        return result_pairs
  
    '''          
        1 : [0]
        2 : [1]
        3 : [2]
        
        '''
        