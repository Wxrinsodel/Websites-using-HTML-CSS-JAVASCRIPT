def add (x,y):
    print(x+y)

def sumthree(x,y,z):
    print(x+y+z)

def sumfour(v,x,y,z):
    print(v+x+y+z)


add(10,20,)
sumthree(10,20,30)
sumfour(10,20,30,50)

#*args มีค่าไม่จำกัด ส่งparamitorได้หลายตัว
def add (*agrs):
    # print(agrs[0]+agrs[1]) #กรณีตัวแปรเดียว
    sum=0
    for i in range(agrs):
        sum+=agrs[i]
    print(sum)
    

add(10,5) #ได้ 15 
add(10,5,20,30)
add(10,5,20,25,30)
add(10,5,20,25,30,"warinsodel")

