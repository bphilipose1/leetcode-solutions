from queue import Queue

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        # Helper dictionaries for conversion
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        prefixDict = {0: "", 1: "Thousand", 2: "Million", 3: "Billion", 4: "Trillion"}

        # Split the number into sections of 3 digits using a queue
        num_queue = Queue()
        temp = num
        while temp != 0:
            rem = temp % 1000
            num_queue.put(rem)  # Enqueue the 3-digit section
            temp //= 1000

        # Helper function to convert a 3-digit section to words
        def threeDigitsToWords(number):
            result = []
            if number >= 100:
                result.append(ones[number // 100] + " Hundred")
                number %= 100
            if 10 <= number <= 19:  # Teens
                result.append(teens[number - 10])
            else:
                if number >= 20:
                    result.append(tens[number // 10])
                    number %= 10
                if number > 0:
                    result.append(ones[number])
            return " ".join(result)

        # Construct the final result
        result = []
        idx = 0
        while not num_queue.empty():
            digits = num_queue.get()  # Dequeue the section
            if digits != 0:  # Skip zero sections
                words = threeDigitsToWords(digits)
                if prefixDict[idx]:
                    words += " " + prefixDict[idx]
                result.insert(0, words)  # Insert at the start to maintain order
            idx += 1

        return " ".join(result)

