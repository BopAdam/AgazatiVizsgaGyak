try:
    a = int(input("a= "))
except:
    a=12

try:
    b = int(input("b= "))
except:
    b=12

try:
    c = int(input("c= "))
except:
    c=24
   
if a+b>c and a+c>b and b+c>a:
    print("Szerkeszthető háromszög")
else:
    print("Nem Szerkeszthető háromszög") 
