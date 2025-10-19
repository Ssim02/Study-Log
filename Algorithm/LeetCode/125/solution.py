# LeetCode 125 - Valid Palindrome

def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum(): # 영문자,숫자인지 판별
            strs.append(char.lower()) # 대소문자를 구분하지 않으므로 소문자로 변경해 append

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
        
    return True # 전부 통과하면 팰린드롬이다
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
