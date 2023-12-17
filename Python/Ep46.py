#Frozen set คือเซตที่ไม่สามารเปลี่ยนแปลงสมาชิกของเซตได้เลย ลบ/แก้/เพิ่มไม่ได้

fruit=frozenset(["Banana","Coconut","Lemon","Giwi" ])
#fruit.add("Cherry") #ขึ้น error 
print(fruit)

for item in fruit:
    print("data=>",item)