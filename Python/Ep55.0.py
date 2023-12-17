# Function return ค่า

"""
1. ไม่มีการรับค่าและส่งค่า #สร้างฟังชั่นทั่วไป มีการกำหนดชื่อและทำงานด้านใน แล้วก็จบ
def name() :

2. มีการรับค่าเข้าไปทำงานในฟังชั่น ส่งค่าผ่านparameter
def name(a,b):

3.มีการรับค่าเข้ามาทำงานและส่งออกมา
def name(a,b):
    return a+b

4. ไม่มีการรับค่าออกมา แต่ส่งค่าออกไป

"""

#แบบที่ 3

def add(a,b):
    return a+b 

print(add(10,20)) 
#x=add(10,20)
#print(x)

# แบบที่ 4 
def add(a,b):
    return a+b

def shownumber():
    return 500

x=shownumber()
print("Number =",x)


def randomnumber(x):
    if x == '100' :
        print("correct")
        return 1000
    else:
        print("incorrect")
        return 0

money=randomnumber("100")
debt=300 
result=money-debt
print("Your presention = ",money)
print("Your change = ", result)

