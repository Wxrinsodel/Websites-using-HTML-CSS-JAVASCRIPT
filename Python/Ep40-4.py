#การค้นหาและนับจำนวนตัวอักษรในสมาชิก

message=["AA","AB","AAB","BBA","BAB","ABA"]
result=[]

for item in message:
    result.append(item.count("A"))
print(result)
