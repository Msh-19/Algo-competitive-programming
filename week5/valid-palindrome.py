class Solution:
    def isPalindrome(self, s: str) -> bool:
         cleaned_phrase = ''.join(char.lower() for char in s if char.isalnum())
         return cleaned_phrase == cleaned_phrase[::-1]
    
    
    

