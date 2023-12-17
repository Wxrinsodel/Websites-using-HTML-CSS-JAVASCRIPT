#Type coversion
x=10
y=3.14
z='20' #เป็น str
print(type(x))

#บวกเลข
#result = x+z  error จ้า > 10+3.14 = 13.14
#result = str(x)+z > '1020'

result = x + int(z)
print(result)

# int => float 
# float => int

print(float(z))