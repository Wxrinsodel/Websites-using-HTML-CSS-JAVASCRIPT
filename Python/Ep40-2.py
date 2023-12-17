#จับคู่คำทักทาย : บุคคล
"""
greeting=["Hi","Hello","Good moring","Goodnight"]
people=["Beb","Rin","Mei","Hendy"]
result=[]
#full normal
for x in greeting:
    for y in people:
        result.append(x+y)
    
print(result)
"""
#แบบลดรูป
greeting=["Hi","Hello","Good moring","Goodnight"]
people=["Beb","Rin","Mei","Hendy"]
result=[x+y for x in greeting for y in people]
print(result)