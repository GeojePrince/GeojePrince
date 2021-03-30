import random
###아래 전체를 반복###
for i in range(1, 5):
    print("밥 무러 가자")
    print("메뉴는?")
#메뉴 변수 나열
    menulist = '학식', '분식', '중식'
    print("1.학식 2.분식 3.중식 4.랜덤")
    menu = input(str(i) + ".입력: ")
#만약에 사용자가 입력한값이 ~면#
    if menu == '1':
        print("학식 먹어라")
    if menu == '2':
        print("분식 먹어라")
    if menu == '3':
        print("중식 먹어라")
    if menu == '4':
        print("랜덤")
        print(random.choice(menulist))
    ###쪼대로를 고르면 위 메뉴중 아무거나###
###여기까지 반복###
