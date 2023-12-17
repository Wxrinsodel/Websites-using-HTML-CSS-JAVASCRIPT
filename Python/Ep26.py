# โครงสร้างการควบคุมแบบทำซ้ำ

i=1 #ตัวนับจำนวนรอบ

'''
summation = 0 #เก็บผลการบวกเลขตามจำนวนรวบ
average = 0
count=int(input('ระบุจำนวนรอบ :'))

while i<=count:
    summation+=i #เก็บผลรวมของ i แต่ละรอบ
    print('รอบที่ = ', i ,'ค่า sum =',summation)
    i=i+1

print('ผลรวมการบวกเลข = ',summation)
print('ค่าเฉลี่ย=',summation/10)

'''
summation=0

for i in range(1,11) : #start,stop-1,step
    summation+=i
    print('รอบที่ = ',i,'sum = ',summation)
print('เฉลี่ย =',summation/10)
print('ผลรวม =',summation)