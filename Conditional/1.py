if True:        # if에 속하는 문장은 모든 문장에 들여쓰기
    print("code1")
    print("code2")
print("code3")

x=1
if x>2:
    print("true")
else:
    print("false")


y=1
if y==1 and x<2:      # and 조건은 그냥 and
    print("true")
else:
    print("false")

if y==1 or x>2:         # or 도 동일 not도 마찬가지
    print("|")
else:
    print("false")

# 조건문 내에서 아무 일도 수행하지 않으려면 
# pass
# 를 사용

# x in 리스트  x not in 리스트
# x in 튜플    x not in 튜플
# x in 문자열  x not in 문자열    같은 조건문도 제공

# if expression:
# elif expression:
# else:
# 과 같은 형태로 if else 내에 또다른 if 문이 중복되는 경우를
# 간단하게 표현 가능