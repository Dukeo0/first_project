def space(text):
    spaces = 0
    for c in text:
        if c == " ":
            spaces +=1
    return spaces

text = """    Akármi és bármi más      """
szokoz= space(text)
print(f"Szóközök száma: {szokoz}")

