#összegzés tétele
#Egész számokat tartalmazó lista elemeit adjuk össze
# max keresése (min ugyanez csak változik a reláció
count = 0
list =[10, 24, 21, 233, 25,234, 8, 172, 25, 14, 9, 8, 5, 5, 5]
max = list[0]
for num in list:
    if max < num:
            max = num
print(max)


# Van egy nevek listája, keresd ki belőle a leghosszabbat!
names = ["John", "Jack", "Józsi Ferike", "Ferenc", "James"]
longest = names[0]
for name in names:
    if len(name) > len(longest):
        longest = name
print(longest)

# Számlálás tétele

# Adott számok halmaza, ezekből a párosokat számoljuk meg

numbers = [-5, 4, 10, 21, 17, 3, 88, 49, 120]
even = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
print(even)

#Eldöntés tétele
#Nevek között van e "John"
names = ["John", "Jack", "Józsi Ferike", "Ferenc", "James"]
van = False
for name in names:
    if name == "John":
        van = True
        break
print(van)

#Szűrés
#Számok listájából válogasd ki egy másik listába a páros számokat
numbers = [-5, 4, 10, 21, 17, 3, 88, 49, 120]
parosok = []
for num in numbers:
    if num % 2 == 0:
        parosok.append(num)
print(parosok)

#Transzformáció (map)
#Van egy név lista, hozzunk létre egy listát, ami a nevek hosszát tartalmazza
names = ["John", "Jack", "Józsi Ferike", "Ferenc", "James"]
name_length = []
for name in names:
    name_length.append(len(name))
print(name_length)