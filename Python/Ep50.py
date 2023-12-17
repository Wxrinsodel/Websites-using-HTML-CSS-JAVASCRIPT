# Global Variable / Local Variable
# ชื่อเหมือนหรือต่างก็ได้ G จะเป็น general Local จะเป็นเฉพาะ
# G = ใช้งานได้เลย L = ต้องเรียกจากด้านในโปรแกรมนั้นๆ

def displaynumber(): #Local
    x=10
    print("Hello = ",x,"ใน") #statement

# main program (Global)
x=20
displaynumber()
print("Hi = ",x,"นอก")

print(x)

# x > ดารา = ทั่วประเทศรู้จัก (Global)
# x > คนธรรมดา = รู้แค่คนรู้จัก (Local)