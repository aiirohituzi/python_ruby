in_str = input("아이디를 입력해주세요.\n")
real_egoing = "egoing"
real_k8805 = "k8805"
if real_egoing == in_str or real_k8805 == in_str:   # and, or, not 그대로 문자를 써넣으면 논리연산 가능
  print("Hello!")
else:
  print("Who are you?")