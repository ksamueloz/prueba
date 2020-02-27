import sys
print (sys.argv)
con1 = sys.argv[1]
con2 = sys.argv[3]

con1 = con1.replace("{","")
con1 = con1.replace("}","")
con2 = con2.replace("{","")
con2 = con2.replace("}","")
print(con1)
print(con2)
con1 = {i for i in con1.split(",")}
con2 = {i for i in con2.split(",")}

union= con1 & con2

print(sorted(union))