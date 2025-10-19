# 정규식 + 슬라이싱 사용

import re

def isPalindrome(s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자를 필터링한다
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1] # 슬라이싱
