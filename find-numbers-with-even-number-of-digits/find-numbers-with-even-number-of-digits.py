class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        result = list(filter(lambda x: self.check_even(x) , nums))
        return len(result)
        
    def check_even(self, num):
        if len(str(num)) % 2 == 0:
            return True
        return False