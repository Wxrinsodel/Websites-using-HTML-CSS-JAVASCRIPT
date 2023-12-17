#Set {}ข้อมูลในเซตซ้ำกันไม่ได้ ใส่ได้ทุกชนิด/แก้ไขข้อมูลสมาชิกได้/ลำดับไม่แน่นอน/ทำงานเร็วกว่า list/tuple เพราะไม่คิดลำดับการทำงาน

"""
List = [], ข้อมูลต่างชนิดกัน , แก้ไขสมาชิกข้อมูลได้ , ข้อมูลซ้ำกันได้ , ซ้ายไปขวา
Tuple = (), ข้อมูลต่างชนิดกัน , แก้ไขสมาชิกข้อมูลไม่ได้ , ข้อมูลซ้ำกันได้ , ซ้ายไปขวา
Set = {}, ข้อมูลต่างชนิดกัน , แก้ไขสมาชิกข้อมูลได้ , ข้อมูลซ้ำกันไม่ได้ , ลำดับไม่แน่นอน , ใช้ Index ไม่ได้

"""
"""
#การสร้าง set แบบปกติ
Fruit={"Mango","Coconut","Apple"}

print(Fruit)

#แบบ constructor

fish=set(["Salmon","selfish"])
print(fish)

"""

#การเพิ่มข้อมูลสมาชิก
"""
Fruit={"Mango","Coconut","Apple"}

Fruit.add("Durian")
Fruit.add("Peanut")

print(Fruit)

"""
#การเพิ่มข้อมูลสมาชิกแบบคราวเดียว
"""

Fruit={"Mango","Coconut","Apple"}

lis=["strawberry","cherry","orange"]
Fruit.update(lis)

print(Fruit)

for i in Fruit:
    print("Information =>",i)

"""
#แสดงจำนวนใน set
"""
Fruit={"Mango","Coconut","Apple"}

lis=["strawberry","cherry","orange"]
Fruit.update(lis)

print(Fruit)

print(len(Fruit))

if "cherry" in Fruit:
    print("Yes")
else :
    print("NO")

print(Fruit)
"""

#การลบข้อมูลใน set

Fruit={"Mango","Coconut","Apple"}

lis=["strawberry","cherry","orange"]
Fruit.update(lis)

Fruit.remove("Mango") #discard ก็ใช้ได้ แต่มันจะไม่ขึ้น error เมื่อหาไม่เจอเหมือน remove
print(Fruit)

