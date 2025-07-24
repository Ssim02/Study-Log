# 백준 1181번 - 단어 정렬

# N개의 단어가 들어오면, 길이가 짧은것부터(길이가 같다면 사전 순으로) 정렬하는 프로그램.
# 단, 중복된 단어가 있다면 하나만 남기고 제거해야 한다. 

N = int(input()) # N개의 단어가 입력이 들어옴
word_list = []
for i in range(N) :
    word = input()
    word_list.append(word)
    

# 조건에 맞추어 정렬한다.
# 1. 중복된 단어 하나만 남기고 제거(set 자료형 사용)
word_list = list(set(word_list))

# 2. 사전 순으로 정렬   
word_list.sort()

# 3. 길이가 짧은 순으로 정렬
word_list.sort(key = len)

# 4. 정렬된 결과물 출력
for word in word_list :
    print(word)
