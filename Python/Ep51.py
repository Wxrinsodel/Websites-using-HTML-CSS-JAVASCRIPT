#การรับ/ส่งค่าเข้ามาที่ function

def mydata(a,b,c): #paramitor ถ้าจะใส่ตัวแปรเพิ่มก็ใช้ , คั่น 
    print("Name =" ,a,"Lastname = ",b,"Age = ",c)

def addition(a,b):
    print(a+b)

x=5
y=9
addition(x,y)
# addition(5,9) #แทนค่าตัวแปรแล้วเรียบร้อย

fname = "jaemin" #Arguments
lname = "na"
age="22"

mydata(fname,lname,age)

#mydata("Jaehyun","Jeong") #เก็บที่ name
#mydata("Jaemin","Na") #เก็บที่ name อีก ทำได้เรื่อยๆ ใส่strก็ได้

#Argument - เป็นค่าที่จะส่งเข้าไปในตัวfunction = fname lname age (Main program)
#Paraneter - ค่าตัวแปรที่รับข้อมูลที่ส่งมาทำงาน = ตรงfunction def [name,Lname,age]