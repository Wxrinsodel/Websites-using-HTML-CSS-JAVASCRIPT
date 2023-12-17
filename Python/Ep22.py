#โปรแกรมคำนวนค่า BMI\#โปรแกรมคำนวนค่า BMI (ดัชนีมวลกาย)
#BMI = น้ำหนัก (Kg) / ส่วนสูง * ส่วนสูง (M)
#convert to int

weight=int(input('ป้อนน้ำหนักของคุณ (kg) :'))
high=int(input('ป้อนส่วนสูงของคุณ (cm) :'))/100
bmi = weight/(high**2)


if bmi<18.0:
    result='low than base'
elif bmi>=18.1 and bmi<=22.9:
    result='slender'
elif bmi>=23.0 and bmi<=24.9:
    result='overweight'
elif bmi>=25.0 and bmi<=29.9:
    result='obesity level 1'
elif bmi>30:
    result='obesity level dangerous'
else :
    result='not clear value'

print('ค่า Bmi = ', bmi ,'ทำนายว่า=',result)


'''
<18 low than base
18.5 - 22.9 = slender
23.0 - 24.9 = more than base
>30 highest >= dangerous

'''