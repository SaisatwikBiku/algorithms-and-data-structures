class Solution:
    def isPalindrome(self, s: str) -> bool:
        low_s = s.lower()

        cleaned = ''.join(ch for ch in low_s if ch.isalnum())

        return cleaned == cleaned[::-1]