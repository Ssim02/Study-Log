# 클래스를 이용한 계산기 프로그램

class FourCal :
    def __init__(self, first, second) : # 생성자
        self.first = first
        self.second = second
    
    def setdata(self, first, second) :
        self.first = first
        self.second = second

    def add(self) :
        result = self.first + self.second
        return result
    
    def mul(self) :
        result = self.first * self.second
        return result
    
    def sub(self) :
        result = self.first - self.second
        return result
    
    def div(self) :
        result = self.first / self.second
        return result

# 클래스 상속
class MoreFourCal(FourCal) :
    def pow(self) :
        result = self.first ** self.second
        return result

class SafeFourcal(FourCal) :
    def div(self) :
        if self.second == 0 : # 나누는 값이 0일경우 0을 리턴하도록 수정
            return 0
        else :
            return self.first / self.second

a = FourCal()
b = FourCal()

a.setdata(4, 2)
b.setdata(3, 8)
a.add()
a.mul()
a.sub()
a.div()
print()
b.add()
b.mul()
b.sub()
b.div()
