# assignment รับและเรียงลำดับข้อมูลตัวเลข

number=[]
while True:
    x=int(input("ป้อนตัวเลขของคุณ : "))
    if x<0:
        break
    number.append(x)

print("ก่อนเรียง=>",number)
print("ค่าที่น้อยที่สุด คือ" , min(number)) #หาค่าน้อยสุด-มากสุด
print("ค่าที่มากที่สุด คือ" , max(number))
print("ผมรวม", sum(number)) 
print("Finish program")