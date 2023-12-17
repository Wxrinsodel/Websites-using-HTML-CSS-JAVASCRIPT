#10 การ remove
"""
number=[1,2,3,4,5,6,7,8,9,10]
fruit=["orange","apple","grape","mango","coconut","lemon"]

fruit.append("watermelon")
fruit.insert(1,"durian")
print("fruits => ", fruit)

fruit.remove("grape")
print("Remove =>", fruit)

"""
#11 การpop เอาอันล่าสุดที่ใส่สุดออกไป
""""
number=[1,2,3,4,5,6,7,8,9,10]
fruit=["orange","apple","grape","mango","coconut","lemon"]

fruit.append("watermelon")
fruit.insert(1,"durian")
print("fruits => ", fruit)

fruit.remove("grape")
print("Remove =>", fruit)
fruit.pop()
fruit.pop()
print("pop =>",fruit)

"""
#12 del การลบ index
"""
number=[1,2,3,4,5,6,7,8,9,10]
fruit=["orange","apple","grape","mango","coconut","lemon"]

fruit.append("watermelon")
fruit.insert(1,"durian")
print("fruits => ", fruit)

fruit.remove("grape")
del fruit # clear the memory

print(fruit)

"""
#13 clere การทำให้ตัวแปรว่าง
"""
number=[1,2,3,4,5,6,7,8,9,10]
fruit=["orange","apple","grape","mango","coconut","lemon"]

fruit.append("watermelon")
fruit.insert(1,"durian")
print("fruits => ", fruit)

fruit.clear()
print(fruit)

"""

#14.copy information
"""
number=[1,2,3,4,5,6,7,8,9,10]
fruit=["orange","apple","grape","mango","coconut","lemon"]

x=[]
print(x)
x=fruit.copy()
print(x)

"""
#15.การรวมข้อมูล
"""
number=[1,2,3,4,5,6,7,8,9,10]
fruit=["orange","apple","grape","mango","coconut","lemon"]

allgroup=number+fruit

print(allgroup)

"""

#16.การแสดงจำนวนสมาชิก
"""
number=[1,2,3,4,5,5,3,9,6,7,8,9,10] #การว่ามีตัวเลขที่ต้องการหากี่ตัว

x=number.count(1)
print(x)

"""

#17 extend การรวมข้อมูลแบบไม่ต้องกำหนดค่าใหม่
number=[1,2,3,4,5,6,7,8,9,10]
fruit=["orange","apple","grape","mango","coconut","lemon"]

number.extend(fruit)
print(number)
