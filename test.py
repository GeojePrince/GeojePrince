import random
menu = '쫄면', '육계장', '비빔밥', '돈까스'
#menu 출력
print(menu)
#랜덤 출력
print(random.choice(menu))

a = '쫄면'
b = '육계장'
c = '비빔밥'
d = '돈까스'

menulist = ['쫄면', '육계장', '비빔밥', '돈까스']
print(len(menulist))
print("메뉴출력")
print("메뉴 개수:",len(menulist))
for i in range(len(menulist)):
    print(menulist[i])

#print(menulist[0])
#print(menulist[1])
#print(menulist[2])
#print(menulist[3])
# print(a)
# print(b)
# print(c)
# print(d)
#menu_list = ['쫄면', '육계장', '비빔밥', '돈까스']
#for i in menu_list:
#    print(i)    