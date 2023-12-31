# 1.string
'''
name = 'warinsodel' # index = ช่องของตัวอักษรที่อยู่ในข้อความนั้นๆ มีค่าเริ่มต้นที่ 0 นับช่องว่างด้วย
#" คือ double code ส่วนใหญ่ใช้กับข้อความยาวๆ
#' คือ single code ใช้กับข้อความไม่ยาวมาก ส่วนใหญ่ใช้อันนี้
print(name[0:8]) #ทำงานก่อนถึงสุดท้าย ':' คือการสั่งให้แสดงผลทั้งหมด แต่ถ้าใส่ตัวเลขข้างหน้ามันจะรันแค่ตัวอักษรนั้นๆ ถ้าใส่ - จะนับจากหลังมาหน้า

'''

# 2.len function คือ การนับความยาวว่ากี่ตัว โดยจะนับช่องว่างด้วย
'''
name = ' warinsodel '
print(len(name))
'''

# 3.strip คือการลบช่องว่างทั้งซ้ายความ ลบซ้ายเติม l ลบขวาเติม r
name = ' warinsodel '
print(len(name))
name=name.rstrip()
print(len(name))


# 4. แปลง case ของ string

'''
name = ' warinsodel '

print(name.lower())

print(name.upper())

print(name.capitalize())

'''

# 5.การแทนที่

name='warinsodel G.4 M.4' 
print(name.replace('4','3.5',1)) #ใส่เลขเพื่อเลือกได้ว่าจะเปลี่ยนกี่ตัว => ('4','3.5',1) 1 = จำนวนตัวที่เราต้องการให้เปลี่ยน ถ้าเจอซ้ำ 2 อัน ก็เปลี่ยนเป็น 2 มันจะเปลี่ยนให้ ถ้าต้องการแค่ 1 ก็ใส่ 1 มันคือจำนวนอ้ะ



# 6. การเช็คข้อความ => true/false

name='ไปอ่านหนังสือ'

x='ไป' in name
if x:
    name=name.replace('ไป','นอน')

print(name)
