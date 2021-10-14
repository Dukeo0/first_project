names = ["John Doe", "Jack Doe", "Jane Doe"]
print(len(names))  # visszaadja az elemek számát
print(names[1])   # visszadja az elem értékét, nullától indul
print(names[::-1])  # visszafele írja ki az elemeket
#Listában lehetnek különböző típusú értékek
akarmi = ["Alma",5,"korte",60]
print(akarmi)

fruits = ["orange"]
fruits.append("apple")
print(fruits)

fruits.insert(0, "banana")
print(fruits)


l = ["aaa", "bbb"]
l += ["ccc"]
print(l)

empty = []


# lista elemei módosíthatóak
numbers = ["x","y","z","z"]
numbers[1] = "a"
print(numbers)

del(numbers[0])
print(numbers)

numbers.remove("z")
print(numbers)

### ez működik stringre is
# if 'e' in name

print("d" in numbers)   # megtalálható e 'd' a numbers-ben
print("z" in numbers)




