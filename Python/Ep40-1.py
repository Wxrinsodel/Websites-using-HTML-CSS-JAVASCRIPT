#เรียงลำดับสมาชิกหลังสุด => มากสุด

fruit=["orange","apple","grape","mango","coconut","lemon"]
print(fruit)
fruit=fruit[::-1] ###
print(fruit)


#หาค่าเลขยกกำลัง

# full normal
number=[1,2,3,4,5,6,7]
for i in range(len(number)):
    number[i]=number[i]**2
print(number)


#ลดรูป
number=[1,2,3,4,5,6,7]
number=[i*i for i in number ]
print(number)
