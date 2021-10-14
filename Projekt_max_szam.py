#adj meg 5 számot, kiírja a számokat, és megkeresi benne a maxot
numbers = []
print("Adj meg öt számot:\n")
while len(numbers) < 5:
    num = input()
    numbers.append(int(num))

print(f"A megadott számok: {numbers}")

max = numbers[0]

for num in numbers:
    print(f"Ezt vizsgáljuk:{num}")
    print(f"Ez most a legnagyobb:{max}")
    if num > max:
        max = num
        print(f"Ez a legnagyobb éppen:{max}\n")

print(f"A legnagyobb szám: {max}")