Tanulo1 = int(input('1 diak erdemjegye:'))
Tanulo2 = int(input('2 diak erdemjegye:'))
Tanulo3 = int(input('3 diak erdemjegye:'))
Tanulo4 = int(input('4 diak erdemjegye:'))
Tanulo5 = int(input('5 diak erdemjegye:'))


# print(Tanulo1,'\n')
# print(Tanulo2,'\n')
# print(Tanulo3,'\n')
# print(Tanulo4,'\n')
# print(Tanulo5,'\n')
jegyek_osszege = float(Tanulo1 + Tanulo2 + Tanulo3 + Tanulo4 + Tanulo5)
print(jegyek_osszege)

jegyek_atlaga = jegyek_osszege / 5
print(f"Matematika dolgozat atlaga: {jegyek_atlaga}")
