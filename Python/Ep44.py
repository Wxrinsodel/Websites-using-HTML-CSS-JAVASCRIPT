#union
#รวม set
"""
FruitA={"Banana","Coconut","Lemon"}
FruitB={"strawberry","Giwi","Cherry"}

AllFruit=FruitA.union(FruitB) #ใช้ FruitA.update(FruitB) ก็ได้
print(AllFruit)

"""
#copy infor
"""
FruitA={"Banana","Coconut","Lemon"}
FruitB={"strawberry","Giwi","Cherry"}
FruitC=FruitA.copy()

print(FruitC)

"""

#Difference แยกว่า A and B ต่างกันยังไง
"""
FruitA={"Banana","Coconut","Lemon","Giwi"}
FruitB={"strawberry","Giwi","Cherry","Coconut"}

FruitC=FruitB.difference(FruitA)
print(FruitC)

"""
#Intersection หาว่า A and B เหมือนกันตรงไหน

FruitA={"Banana","Coconut","Lemon","Giwi"}
FruitB={"strawberry","Giwi","Cherry","Coconut"}
print(FruitA)
FruitC=FruitB.intersection(FruitB)
print(FruitC)

#subset = set ย่อย คือการเอา set มาเปรียบเทียบกัน



  