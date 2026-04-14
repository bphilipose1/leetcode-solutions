class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        idx = 0
        result = []
        while idx < len(intervals)-1:
        
            if intervals[idx][1] >= intervals[idx+1][0]:
                result.append([intervals[idx][0], intervals[idx+1][1]])
                idx += 2
            else:
                result.append(intervals[idx])
                idx += 1
        if idx == len(intervals) - 1:
            result.append(intervals[idx])
        return result