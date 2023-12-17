#Dict คือตัวที่รวมความสามารถของ set และ tuple // key การเข้าถึงข้อมูล ,value ค่าของข้อมูล

#สร้างแบบปกติ = ชื่อตัวแปร= {key:value,key:value}

Colors= {"red":"สีแดง","Green":"สีเขียว","Yellow":"สีเหลือง"}
City={"bangkok":"กรุงเทพ"}
Vocab={"obey":"เชื่อฟัง"}

print(colors.get["Yellow"])
print(colors["Green"])

#แบบconstucture

pets=dict(cat="แมว",dog="หมา",duck="เป็ด")
print(pets["dog"]) #ใส่ตัว key เท่านั้น (ตัวแปรแรก)
print(colors.get("Red")) #ใส่ตัว key เท่านั้น (ตัวแปรแรก)


#การเพิ่ม
pets[100]="Measurement" 
pets.update({"rabbit":"กระต่าย","fish":"ปลา","snake":"งู"})
print(pets)


#การวนลูป

colors= {"Red":"สีแดง","Green":"สีเขียว","Yellow":"สีเหลือง"}
colors.update({"blue":"สีฟ้า","pink":"สีชมพู"})

for item in colors:
    print(item) 
# ผลออกมาแค่ตัว key อยากได้ value ใส่ colors.value



#การลบ

colors= {"Red":"สีแดง","Green":"สีเขียว","Yellow":"สีเหลือง"} 

colors.pop("Red")
colors.popitem()  #จะลบตัวท้าย
print(colors)

#การลบสมาชิกทั้งหมด ถ้าจะลบตัวแปลใช้ del
colors.clear()
del colors
print(colors)


#copy

colors= {"Red":"สีแดง","Green":"สีเขียว","Yellow":"สีเหลือง"}
colors.update({"blue":"สีฟ้า","pink":"สีชมพู"})
x=colors.copy()
print(x)


