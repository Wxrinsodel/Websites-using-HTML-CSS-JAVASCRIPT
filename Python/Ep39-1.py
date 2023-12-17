# assignment หากลุ่มเลขคู่/เลขคี่

number=[]
odd=[]
even=[]
while True:
    x=int(input("ป้อนตัวเลขของคุณ : "))
    if x<0:
        break
    if x%2 == 0:
        even.append(x)
    else :
        odd.append(x)
    number.append(x)

print("ตัวเลขทั้งหมด => " , number)
print("odd number => " , even)
print("even number => " , odd)
