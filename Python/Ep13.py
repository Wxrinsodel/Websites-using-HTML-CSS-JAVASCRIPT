#โปรแกรมคำนวนค่า BMI (ดัชนีมวลกาย)
#BMI = น้ำหนัก (Kg) / ส่วนสูง * 2 (M)

#convert to int

weight=int(input('ป้อนน้ำหนักของคุณ (kg) :'))
high=int(input('ป้อนส่วนสูงของคุณ (cm) :'))

#process
#cm=>m
high/=100
#calculate bmi
BMI = weight/(high**2)

#output
print('BMI = ',BMI)