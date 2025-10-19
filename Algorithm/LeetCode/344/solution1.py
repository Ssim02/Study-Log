# LeetCode 344 - Reverse String

# Two Pointer Swap

def reverseString(s: str) -> None:
    left, right = 0, len(s) - 1 # left, right : 이용할 두개의 포인터

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

