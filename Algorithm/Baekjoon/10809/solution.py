# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 
s = str(input())

# 알파벳 소문자 리스트를 만들 때 아스키코드로 사용할 값
alpha_i = 97

# 모든 알파벳 소문자가 들어간 리스트 생성
alphabat_list = []
for i in range(26) :
    alphabat_list.append(chr(alpha_i))
    alpha_i += 1

# 결과값을 출력할 리스트 생성
result = []
for i in range(26) :
    result.append(-1)

# 알파벳이 단어에 포함되어 있지 않다면 -1을 출력. 

alpha_i = 97 # 반복문 돌며 증가했던 값 다시 초기화

# "처음으로 등장하는 위치" -> 같은 알파벳이 두 개 이상 주어지면,
# 처음 위치만 기억하도록 해야 함. 중복 제거하는 부분을 언제?
for i in range(len(alphabat_list)) :
    for sub_i in range(len(s)) :
        if alphabat_list[i] == s[sub_i] :
            if result[i] == -1 :
                result[i] = sub_i

# 각각의 알파벳에 대해서, 각 알파벳이 처음 등장하는 위치를 공백으로 구분해서 출력.
# 리스트 형태로 출력하면 안되니까..
for i in range(len(result)) :
    print(result[i], end=" ")
