#Tuple เหมือนลิสต์เลย แต่เปลี่ยนแปลงข้อมูลไม่ได้และต่างกันตรงเคื่องหมาย

#1.การนิยาย, constructor
"""
tup=tuple((1,2,3,4,"wr",True,0.99))
lis=list([1,2,3,4,"wr",True,0.99])
print(tup)
print(lis)

"""

#2.การเข้าถึงข้อมูล / แบบกำหนดช่วง
"""
tup=tuple((1,2,3,4,"wr",True,0.99))

print(tup[-2]) #[:]

"""
#3.การแก้ไขข้อมูล => แปลงเป็น list
"""
tup=((1,2,3,4,"wr",True,0.99))
print("ก่อนแก้ไข =>", tup)
lis=list(tup)
lis[0]="Long"

tup=tuple(lis)
print("หลังแก้ไข =>", tup)

"""
#4.การแสดงผลที่ Loop
"""
tup=((1,2,3,4,"wr",True,0.99))

for item in tup:
    print("สมาชิก = ",item)

"""
#5.การตรวจสอบข้อมูล
"""
tup=((1,2,3,4,"wr",True,0.99))

if "wr" in tup:
    print("เป็นสมาชิก")
else :
    print("ไม่เป็นสมาชิก")

"""

#6.การนับจำนวนสมาชิก
"""
tup=((1,2,3,4,"wr",True,0.99))
print(len(tup))

"""
#7. len ทำงานร่วมกับ loop for
"""
tup=((1,2,3,4,"wr",True,0.99))

for item in range(len(tup)):
    print(tup[item])

"""
#8. การสร้างข้อมูล
"""
tup=(1,2,3,4,"wr",True,0.99)

มีสองแบบ
1. x=()
   print (type(x))
2. x=tuple()
   print(x)
"""

#9.การเพิ่มข้อมูล
"""
tup=(1,2,3,4,"wr",True,0.99)

name=("Oikawa","Kuroo",)
new=("Hinata","Gojo")

name+=new
print(name)
"""

#10. การทำงานร่วมกับ List
"""
tup=(1,2,3,4,"wr",True,0.99)

lis=list(tup)
lis[1]='Bangkok'

tup=tuple(lis)
print(tup )
"""
#11.การลบข้อมูลโดยใช้ Del

"""
tup=(1,2,3,4,"wr",True,0.99)
del tup
print(tup)
"""
#11.การลบข้อมูลโดยใช้ list
"""
tup=(1,2,3,4,"wr",True,0.99)
lis=list(tup)
lis.remove(2)
print(lis)
"""
#12.count นับจำนวน
"""
tup=(1,2,3,4,"wr",True,0.99)

x=tup.count(3)
print(x)
"""
#12.index หาว่าอยู่ตรงไหน
"""
tup=(1,2,3,4,46,29,45,15,78,36,49,0.99)

x=tup.index(3)
print(x)
"""

#13.การ sort ข้อมูล

tup=(1,2,3,4,46,29,45,15,78,36,49,0.99)

lis=list(tup)
lis.sort()
tup=tuple(lis)
print(tup)