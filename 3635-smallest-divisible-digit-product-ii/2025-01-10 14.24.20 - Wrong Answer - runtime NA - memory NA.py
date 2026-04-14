class Solution: #THIS WAS A SMALL LLM TEST, I DID NOT COMPLETE THIS
    def smallestNumber(self, num: str, t: int) -> str:
        n = int(num)
        
        # Set to store seen numbers
        seen = set()
        
        while True:
            # Convert integer back to string for digit manipulation
            str_n = str(n)
            
            # Check if number is zero-free and product of digits is divisible by t
            product = 1
            for digit in str_n:
                product *= int(digit)
            
            if product % t == 0 and '0' not in str_n:
                return str_n
            
            # If we've seen this number before, skip it
            if n in seen:
                continue
            
            # Add current number to the set of seen numbers
            seen.add(n)
            
            # Increment number until we find the smallest satisfying conditions
            n += 1
            
            # If number becomes too large, return -1
            if n > int(num) * 10:
                return "-1"