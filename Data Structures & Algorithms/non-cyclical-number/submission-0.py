class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()

        value = self.sumOfSquaresOfDigits(n)
        while (value not in cache):
            if (value == 1):
                return True
            cache.add(value)
            value = self.sumOfSquaresOfDigits(value)
        
        return False
    
    def sumOfSquaresOfDigits(self, number: int) -> int:
        value = 0

        while (number != 0):
            digit = number % 10
            value += digit*digit
            number = number // 10
        
        return value