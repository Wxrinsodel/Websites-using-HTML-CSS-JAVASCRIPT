#จับคู่สินค้ากับราคา

fruit=["orange","apple","grape","mango","coconut","lemon"]
price=[20,15,30,25,35,27]

for x,y in zip(fruit,price):
    print("product = ",x , "price = ",y)