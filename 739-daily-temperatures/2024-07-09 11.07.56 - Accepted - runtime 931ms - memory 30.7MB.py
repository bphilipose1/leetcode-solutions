class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        min_stack = []
        result = [0] * len(temperatures)
        for curr_index, curr_temp in enumerate(temperatures):
            def store_ans(index1, index2):
                dist = index2 - index1
                result[index1] = dist

            #first check if stack is not empty, then check if input val is greater than whats in the stack
            while min_stack and (temperatures[min_stack[-1]] < curr_temp):
                #if it removes top value, pop it and store ans
                store_ans(min_stack.pop(), curr_index)
            
            #then store input
            min_stack.append(curr_index)
        
        return result



