#โครงสร้างควบคุม (control Structure)
#1.แบบลำดับ
#2.แบบเลือก
#3.แบบทำซ้ำ
#if คือการระบุเงื่อนไข โดยเงื่อนไขต้องเป็นจริง

age=int(input('ป้อนอายุของคุณ'))

#name='warinsodel'
#print(type(age>=15))
#print(name=='warinsodel')

if age>=15:
    print('คำนำหน้าเป็นนางสาว/นาย') #ต้องเว้นวรรคแบบนี้เสมอ
    print('จบโปรแกรมด้านใน if')
    
print('จบโปรแกรม') #ขอบเขตของอีฟอยู่แค่ 2 บรรทัด

