class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = ([char.lower() for char in s if char.isalnum()])
        for i in range(int(len(cleaned_text)/2)):
            if(cleaned_text[i] != cleaned_text[len(cleaned_text) - 1 - i]):
                return False
        return True