age=int(input('ป้อนอายุของคุณ :')) 

#elif คือตัวเลือกรองจาก If โปรแกรมจะรันตรง If ก่อน
#else คือ

if age>=15 or age<=20:
    print('วัยรุ่น')
elif age>=20 or age<=29:
    print('วัยหนุ่มสาว')
elif age>=30 or age<=39:
    print('วัยผู้ใหญ่')
elif age>=80:
    print('วัยชรา')
else :
    print('วัยเด็ก')

print('จบโปรแกรม')

# 15-20 => วัยรุ่น
# 21-29 => วัยผู้ใหญ่
# 30-39 => วัยทำงาน

