###아래 전체를 반복###
for i in range(1, 4):
    print("밥 무러 가자")
    print("메뉴는?")
    print("1.학식 2.분식 3.중식")
    menu = input(str(i) + ".입력: ")
#만약에 사용자가 입력한값이 ~면#
    if menu == '1':
        print("학식 먹어라")
    if menu == '2':
        print("분식 먹어라")
    if menu == '3':
        print("중식 먹어라")
###여기까지 반복###
