# 1. új név rögzítése
# 2. Nevek listázása
# 3. kilépés

value = 0
name_list = []
menu_text= """
1. Új név rögzítése
2. Nevek listázása
3. Kilépés """
while value != 3:
    print(menu_text)
    value = int(input())
    if value > 3 or value < 1:
        print("Helytelen bemenet")
    if value == 1:
        Name = input("Add meg a nevet:\n")
        name_list.append(Name)
    if value == 2:
        name_out = ""
        length = len(name_list)
        counter = 1
        for name in name_list:
            if counter != length:
                name_out += name +", "
                counter += 1
            else:
                name_out += name
        print(f"Nevek listája: {name_out}\n")