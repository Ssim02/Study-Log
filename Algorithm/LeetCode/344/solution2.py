# reverse()

from typing import List

# 문제 조건이 리턴값 없이 문자열 내부 조작이므로, 리턴 타입을 None으로 지정해 아무것도 리턴하지 않겠다고 지정.
def reverseString(s: List[str]) -> None: # -> : 함수의 반환 타입을 명시하겠다는 신호
    s.reverse()
