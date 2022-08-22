class Solution:
    # t: O(N), t: O(N)
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    # t: O(N), t: O(N)
    def isPalindrome2(self, x: int) -> bool:
        if x > 0:
            tmp = x
            reverse = []
            
            while tmp > 0:
                digit = tmp % 10
                reverse.append(digit)
                tmp //= 10

            original = reverse[::-1]
            return org_digits == reverse_digits
        elif x == 0:
            return True 
        else:
            return False 