"""
primitive
a=1
a1=2
a2=3
a3=4
a4=5
# non primitive : LIST
"""

#1. นิยาม
"""
number=[] #[] คือลิสต์ว่าง จะยัดไรเข้าไปก็ได้
number=[1,2,3,4,5,6] # list มีสมาชิก 1,2
name=["Mr.A","Mr.B","Mr.C"] # list name members
all=[10,"Mr.A",True,3.14,-56]

name=list(["Mr.A","Mr.B","Mr.C"]) #รูปแบบ constructor
print(name)
print(all)
print(number)

"""
#2. การเข้าถึงข้อมูลแบบเดี่ยว/แบบกำหนดช่วง = เอา : มาขั้น
'''
print(all[1:4]) #ก่อน1ไม่ถึง 4

'''
#3. การแก้ไขข้อมูล
"""
# ชื่อตัวแปร[index ] = 'ข้อมูลที่แก้ไข
number=[1,2,3,4,5,6]
print("ก่อนแก้ไข => ",number)
number[4]=9
number[-1]=10
print("หลังแก้ไข => ",number)

"""


#4. แสดงผลด้วย Loop
"""
number=[1,2,3,4,5,6,7,8,9,10]

sum=0
for x in number:
    sum+=x #sum=sum+x
print(sum)

"""
#5.การตรวจสอบข้อมูล
"""
number=[1,2,3,4,5,6,7,8,9,10]
fruit=["orange","apple","grape","mango","coconut","lemon"]

if "orange" in fruit:
    print("เป็น")
else:
    print("ไม่เป็น")
"""

#6.การนับจำนวนสมาชิก
"""
number=[1,2,3,4,5,6,7,8,9,10]
fruit=["orange","apple","grape","mango","coconut","lemon"]
name=["A","B"]
print(len(number))
print(len(fruit))
"""
#7.การใช้ Len ร่วมกับ Loop For
'''
number=[1,2,3,4,5,6,7,8,9,10]
fruit=["orange","apple","grape","mango","coconut","lemon"]

for i in range(len(fruit)):
    print(fruit[i])
'''

#9.การเพิ่มข้อมูล
"""
number=[1,2,3,4,5,6,7,8,9,10]
fruit=["orange","apple","grape","mango","coconut","lemon"]

print("ก่อนเพิ่ม", fruit)

fruit.append("watermelon")

print('หลังเพิ่ม=>' ,fruit)

#insert (index, new member)
print("หลังเพิ่ม=>" , fruit)
fruit.insert(0, "durian")
print("หลังแทรก=>" , fruit)

"""