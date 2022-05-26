class Solution:
    def intToRoman(self, num: int)->str:
        
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        
        roman_digits = []
        for value, symbol in digits: 
            
            if num == 0:
                break
            
            count, num = divmod(num, value)
            roman_digits.append(symbol * count)
        
        return "".join(roman_digits)
    # t: O(1) there is a hard upper limit for the size of roman array
    # s: O(1) amount of memory does not change with the input, therefore it is constant  

    # Segmented solution, the same time complexity
    def intToRoman(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return (thousands[num // 1000] + hundreds[num % 1000 // 100] 
               + tens[num % 100 // 10] + ones[num % 10])




''' 
Max Product of Subarray 
x = divmod(5, 2)
x will be a tuple of (2, 1)
'''