#아래 전체를 반복#
for i in range(1, 4):
    print("뭐먹을까")
    print("뭐먹을지 골라라.")
    print("1. 머거스 2. 짜장면 2. 3. 햄버거")
    a = input("입력: ")
    print("당신이 입력한 값은? ", a)
#만약에 1번이면#
    if a == "1":
        print("머거스")
#만약에 2번이면#
    if a == "2":
        print("짜장면")
#만약에 3번이면#        
    if a == "3":
        print("햄버거")
#여기까지 반복#       
