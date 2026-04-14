class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        idx = 0
        result = []
        while idx < len(intervals)-1:
        
            if intervals[idx][1] >= intervals[idx+1][0]:
                #take lesser of bottom
                if intervals[idx][0] < intervals[idx+1][0]:
                    bot = intervals[idx][0]
                else:
                    bot = intervals[idx+1][0]
                
                #take higher of top
                if intervals[idx][1] > intervals[idx+1][1]:
                    top = intervals[idx][1]
                else:
                    top = intervals[idx+1][1]

                result.append([bot, top])
                idx += 2
            else:
                result.append(intervals[idx])
                idx += 1
        if idx == len(intervals) - 1:
            result.append(intervals[idx])
        return result