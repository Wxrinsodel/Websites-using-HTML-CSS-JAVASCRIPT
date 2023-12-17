# Function return ค่า 2
def randomnumber(x):
    if len(x)<3:
        return 
    if x == '100' :
        print("correct")
        return 1000
    else:
        print("incorrect")
        return 0

money=randomnumber("500")
print("Your presention = ",money)
