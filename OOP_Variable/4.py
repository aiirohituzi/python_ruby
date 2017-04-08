class C(object):
    def __init__(self, v):
        self.__value = v    # __를 변수명 앞에 붙일경우 인스턴스 바깥에서 접근 불가
    def show(self):
        print(self.__value)
c1 = C(10)
#print(c1.__value)  # 에러발생, 접근 불가
c1.show()