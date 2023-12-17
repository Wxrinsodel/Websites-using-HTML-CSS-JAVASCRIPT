#subset = set ย่อย คือการเอา set มาเปรียบเทียบกันว่าเป็นสมาชิกของเซตมั้ย
#Superset คือการเช็คว่าตัวแปรแรกเป็นหัวข้อใหญ่ของตัวแปรสองมั้ย

fish={"Dolphin","Gold fish","Salmon","Shark","Wale","Orca"} #Superset

X={"Dolphin","Salmon"}#subset
Y={"Shark","Wale"}

print(fish.issuperset(X))