class Cal(object):
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1
c1 = Cal(10,10)
print(c1.add())
print(c1.subtract())
c1.setV1('one')     # 원하지 않는 데이터타입의 입력을 예방, 그러나 여전히 변수로의 직접 접근은 막을 수 없음
c1.v2 = 30
print(c1.add())
print(c1.subtract())