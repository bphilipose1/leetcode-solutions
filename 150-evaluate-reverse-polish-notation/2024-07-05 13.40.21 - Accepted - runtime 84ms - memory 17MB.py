class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp = tokens
        operators = ['+', '-', '*', '/']
        x = 0
        while x < len(temp) and len(temp) > 1:
            #print('x:', x, '-', temp)
            #if it finds an operator
            val = temp[x]
            index = x
            if val in operators: 
                #print('completed sipmlification', temp[index-2], temp[index-1], val)
                #find what operation to complete, and take the 2 values behind it
                if val == '+':
                    out = int(temp[index-2]) + int(temp[index - 1])
                elif val == '-':
                    out = int(temp[index-2]) - int(temp[index - 1])
                elif val == '*':
                    out = int(temp[index-2]) * int(temp[index - 1])
                else:
                    out = int(int(temp[index-2]) / int(temp[index - 1]))
                #then remove the operator and right number
                temp.pop(index)
                temp.pop(index - 1)
                #replace the operator with the output values
                out = str(out)
                temp[index - 2] = out

                #set x to that new number
                x = index - 2
                
            x+=1
            
        return int(temp[0])

        #time complexity is O(n)
            

        