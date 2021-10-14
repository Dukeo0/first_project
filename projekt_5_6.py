my_str = "Elemér"
vanbenne = False
for c in my_str:
    if c == "e":
        vanbenne = True
        break
if vanbenne:
    print("Van benne 'e' betű")
else:
    print("Nincs benne 'e' betű")
