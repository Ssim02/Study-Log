# 재귀호출 이용해서 최대공약수 구하기
def gcd(a, b) :
        if a * b == 0 : # 탈출 조건(둘중에 하나가 0인 경우)
            return a + b
        if a > b :
            return gcd(b, a - b)
        else :
            return gcd(a, b - a)
        
print(gcd(8, 12))
        
