# เกมทายลูกเต๋า
#1,2,3,4,5,6

import random
#สุ่มเลขลูกเต๋า
myrandom = random.randrange(1,7) #1 - 6
k=1
correct=False
print("คุณมีโอกาสตอบเพียง 3 ครั้ง \n")
while True:
    number=int(input("ป้อนคำตอบของคุณ = "))
    correct=(number==myrandom) # T/F
    if not correct :
        if(number>myrandom):
            print("น้อยกว่า")
        if(number<myrandom) :
            print("มากกว่า")

    if correct :
        print("ยินดีด้วยคุณได้รับเงินรางวัล 1 ล้านบาท")
        break
    if number<0 or k==3:
        break
    k+=1

if not correct:
    print("เสียใจด้วยนะ")
    print("เฉลย = ", myrandom)