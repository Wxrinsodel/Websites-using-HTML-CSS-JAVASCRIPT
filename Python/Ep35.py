# ตารางหมากฮอต

"""
xxx
xxx
xxx

x=Brown
o=white
"""
'''
number=int(input("ป้อนขนาด =")) #5 = แสดงผลเป็น 01234

for row in range(number):
    for column in range(number):
        if column%2 == 0 :
            print("x",end="")
        else :
            print("o",end="")
    print(" ") #ได้ xo อย่างเดียว

'''

number=int(input("ป้อนขนาด ="))

for row in range(number):
    for column in range(number):
        if (row+column)%2 == 0 : 
            print("x",end="")
        else :
            print("o",end="")
    print(" ") #ได้ xo อย่างเดียว

