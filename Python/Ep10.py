#ตัวดำเนินการทางตรรกศาสตร์
# And/or/not
# and เป็นจริงเมื่อทั้งสองฝั่งเป็นจริง
# or ฝั่งใดฝั่งหนึ่งเป็นจริง
# not ขั่วตรงข้าม

# แบบ 1 ('ค่า x มากกว่า y หรือไม่? : ', x>y)
# แบบ 2 ('ค่า x น้อยกว่า y หรือไม่? : ', x<y)
# แบบ 3 ('ค่า x เท่ากับ y หรือไม่? : ', x==y)
# แบบ 4('ค่า x ไม่เท่ากับ y หรือไม่? : ', x!=y)

#คำตอบที่ได้จะมี True & False

from re import X


x = (5>10) #ค่า x = bool > F
y = (10==5) #ค่า y = bool > F


#z=5>10 and (10==5)
z = (10>5) or (10!=5)

print(z)