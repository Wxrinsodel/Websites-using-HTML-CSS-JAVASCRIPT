# Keyword Arguments

def displayData(fname,Lname,City):
    print("Name = ",fname)
    print("Lastname = ",Lname)
    print("City =",City)

displayData("KUROO","Sawamura","Tokyo")
displayData(City="Bangkok",Lname="Apichon",fname="Supawadee") #ถ้าจะสลับตำแหน่งให้เชื่อมparamitorไว้ มันจะได้ไม่หลง



# Default Parameter
#การกำหนดค่าเริ่มต้นหากไม่มีการป้อนparameterนั้น => Bangkok
def displayData(fname,Lname,City="Bangkok"):
    print("Name = ",fname)
    print("Lastname = ",Lname)
    print("City =",City)

displayData("Tooru","Oikawa",)
displayData(Lname="Apichon",fname="Supawadee") #parameterไม่ครบ โปรแกรมไม่รัน นอกจากจะกำหนดค่าเริ่มต้นไว้แล้ว แบบนี้จะฟิคคำตอบ\



#การโยนlist/tuple เข้ามา
def displayFruit(item):
    for i in range(len(item)):
        print("ผลไม้ชิ้นที่ ",i+1," = ", item[i])

def displayVetTuple(item):
    for i in range(len(item)):
        print("ผลไม้ชิ้นที่ ",i+1," = ", item[i])


Fruit=["Mango","Coconut","Lemon"]
Vet=("carrot","Tamato","cucumber")
displayFruit(Fruit)
displayVetTuple(Vet)
