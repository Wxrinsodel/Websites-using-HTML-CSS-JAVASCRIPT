# pass ใช้กับกรณีคิดลักษณะการทำงานไม่ออก

age=int(input('ป้อนอายุของคุณ'))

if age<=15:
    if age==15:
        pass
    elif age==14:
        pass
    elif age==13:
        pass
    else :
        print('ประถม')
       
else :
    print('ม.ปลาย')

print('จบโปรแกรม')