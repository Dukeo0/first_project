my_str = "joistenmegaldja"
ujstring = ""
count = 0
length = len(my_str)
for c in my_str:
    if count == length -1:
        ujstring += c
        break
    ujstring += c + "*"
    count += 1

print(f" {ujstring}")
