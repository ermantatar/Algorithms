# Algorithm
# - First of all, record all roman characters and their values as [(value, roman char)...()] array of tuples. 
# - For loop, this sorted(highest value, to lowest value) array, then do count, rest_num = divmod(num, value), and add that character, count times to the result. count * character
# - Continue like this until you have no more origin num left. 
# - Return the result array with turning into a string with "".join(result_array)

class Solution:
    # t: O(1) there is a hard upper limit for the size of roman array
    # s: O(1) amount of memory does not change with the input, therefore it is constant
    def intToRoman(self, num: int)->str:
        
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        
        roman_digits = []
        for value, symbol in digits: 
            # if no more num, break it here. 
            if num == 0:
                break
            
            count, num = divmod(num, value) # divmod(5, 2) -> (2, 1)
            roman_digits.append(symbol * count)
        
        return "".join(roman_digits)
      

    # Segmented solution, the same time complexity
    def intToRoman(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return (thousands[num // 1000] + hundreds[num % 1000 // 100] 
               + tens[num % 100 // 10] + ones[num % 10])



