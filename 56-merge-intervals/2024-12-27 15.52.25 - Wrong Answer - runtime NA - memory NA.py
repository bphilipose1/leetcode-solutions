class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = [intervals[0]]
        i = 1
        while i < len(intervals):
            p2 = intervals[i] #see if the new interval in the scope can be merged
            p1 = result[-1] #the last interval to see if further merges can occur
            if p1[1] >= p2[0]:#began merging
                temp_min = min(p1[0], p2[0])
                temp_max = max(p1[1], p2[1])
                temp_res = [temp_min, temp_max]
                result[-1] = temp_res
                i += 1
            else: #append last result, and start new temp_res
                result.append(p2)
                i += 1
                
        print(result)
        return result