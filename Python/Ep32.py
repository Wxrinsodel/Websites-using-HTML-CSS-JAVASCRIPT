#ค้นหาตัวเลขมากสุด น้อยสุด

max , min = 0 , 999

while True :
    number=int(input("ป้อนตัวเลขของคุณ :")) #กระโดดออกจากลูป
    if number<0 : #กระโดดออกจากลูป
        break
    if number>max :
        max=number
    if number<min :
        min=number

print("ค่าสูงสุด =",max)
print("ค่าต่ำสุด =",min)
