#นำค่าใน Tuple => ตัวแปร
"""
tup=(10,20,30)
a,b,c=tup
print(a)
print(b)
d=a+c
print(d)
"""
#สลับ tuple
"""
x=(50,60)
y=(88,95)

x,y=y,x

print(x , y)
"""
#แปลง tuple => string
"""
ch=('w','a','r','i','n')
name="".join(ch)
print(name)

"""
#การ reverse tuple

x=(100,20,65,32,48)
y=reversed(x)
print(tuple(y))