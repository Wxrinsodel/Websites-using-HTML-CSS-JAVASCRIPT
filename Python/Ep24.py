# 7. การต่อ str +

fname = 'warin'
lname = 'sodel'
age = '16'

#แบบ 1 => fullname=fname+lname+age print(fullname)

print('ชื่อต้น :'+fname+'\tนามสกุล :' +lname+'\tอายุ : '+age) #แบบ 2

# 8. การจัดรูปแบบการแสดงผล format + {}
'''
fname = 'warin'
lname = 'sodel'
age = '16'
salary=320000
'''

text="ชื่อต้น :{}\tนามสกุล :{} \tอายุ :{}\tอาชีพ:" #มาร์กตำแหน่งการแทนที่แล้ว จะใส่เลขก็ได้ตามลำดับตามต้องการ แต่แบบนี้ก็ได้

print(text.format(fname,lname,age,'student'))

# 9. การนับจำนวนคำในประโยค

'''
fruit='ไปซื้อผลไม้ มีทุเรียน มังคุด ข้าวเหนียวมะม่วง ที่ตลาด แวะไปสวนมังคุดด้วย'
print(fruit.count('มังคุด'))

'''

# 10. เช็คคำขึ้นต้น
'''
name='Mr. shelock'

if name.startswith('Mr.') :
    print('male')
else :
    print('female')

print(name.startswith('Mr.')) # cheak T/F
'''

