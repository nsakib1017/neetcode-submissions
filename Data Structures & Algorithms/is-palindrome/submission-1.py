class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_list = []
        for i in s:
            if i.isalnum():
                char_list.append(i.lower())
        for i in range(0, int(len(char_list)/2)):
            j = (len(char_list) - i) - 1
            if char_list[i] != char_list[j]:
                return False
        return True