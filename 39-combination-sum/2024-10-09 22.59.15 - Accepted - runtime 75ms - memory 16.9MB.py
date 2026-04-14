class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def recAdd(i, cur_sum, sub_res):
            #got a solution
            if cur_sum == target and sub_res not in result:
                result.append(sub_res.copy())
                print(result)
                return

            if i >= len(candidates) or cur_sum > target:
                return
            num = candidates[i]
            #include adding num
            sub_res.append(num)
            recAdd(i, cur_sum + num, sub_res)

            #dont include adding num
            sub_res.pop()
            recAdd(i+1, cur_sum, sub_res)

            return
        recAdd(0, 0, [])
        return result