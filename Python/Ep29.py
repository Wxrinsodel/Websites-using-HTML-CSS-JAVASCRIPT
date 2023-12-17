#break / continue

from ast import Continue

#1
'''
i=1
while i<=10:
    print('รอบที่ =', i)
    i+=1
else:
print("Finish program")
'''

#การใช้ break กระโดดออกจากลูบ

'''
i=0
while i<=10:
    print("รอบที่ =",i)
    if(i==5):
        break
    i+=1
else:
    print("Finish program")
'''

#การใช้ CONTINUE อยู่ในลูปแต่กระโดดข้ามตามที่เรากำหนด

'''
i=0
while i<=10:
    i+=1 #11 มาจากตรงนี้
    if(i%2 == 0): #อะไรหาร 2 = 0 กระโดดข้าม
        continue
    print('รอบที่ = ',i)

print("Finish program")
'''
#EX

for i in range(1,11):
    if(i%2 == 0): #อะไรหาร 2 = 0 กระโดดข้าม
        continue
    print(i)

print("Finish program")